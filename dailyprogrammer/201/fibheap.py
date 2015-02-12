class FibNode(object):
	def __init__(self, k, v):
		self.v = v
		self.k = k
		self.parent = None
		self.child = None
		self.degree = 0
		self.mark = False
		self.right = None
		self.left = None
		self.sibling = None
		self.timer = None

	def __str__(self):
		return '({},{})'.format(self.v,self.k)

class FibHeap(object):
	def __init__(self):
		self.min = None
		self.roots = None
		self.n = 0
	
	def __len__(self):
		return self.n

	def Count(self):
		return len(self)

	def Clear(self):
		self.min = None
		self.roots = None
		self.n = 0

	def  __bool__(self):
		return bool(len(self))

	def removeChild(self, node, parent):
		if parent.child == node:
			parent.child = node.right
		if node.right:
			node.right.left = node.left
		if node.left:
			node.left.right = node.right

	def root(self, node):
		node.left, node.right, node.parent = None, None, None
		node.right = self.roots
		if node.right:
			node.right.left = node
		self.roots = node

	def unroot(self, node):
		if self.roots == node:
			self.roots = node.right
		if node.right:
			node.right.left= node.left
		if node.left:
			node.left.right = node.right
		node.left, node.right, node.parent = None, None, None

	def Enqueue(self, k, v):
		node = FibNode(k,v)
		self.root(node)
		if self.min == None or self.min.k > k:
			self.min = node
		self.n += 1
		return node

	def Dequeue(self):
		node = self.min
		if node:
			self.unroot(node)
			child = node.child
			while child:
				nextChild = child.right
				self.root(child)
				child = nextChild
			if self.n == 1:
				self.min = None
				self.roots = None
			else:
				self.consolidate()
			self.n -= 1
		return node

	def consolidate(self):
		working = {}
		node = self.roots
		while node:
			nextNode = node.right
			d = node.degree
			while d in working:
				target = working[d]
				if node.k > target.k:
					node, target = target, node
				self.link(node, target)
				del working[d]
				d += 1
			working[d] = node
			node = nextNode
		self.min = None
		for d in working:
			if not self.min or working[d].k < self.min.k:
				self.min = working[d]

	def link(self, node, target):
		self.unroot(target)
		target.right = node.child
		if target.right:
			target.right.left = target
		node.child = target
		node.degree += 1
		target.mark = False
		target.parent = node

	def decreaseKey(self, node, k):
		if k >= node.k:
			return
		node.k = k
		parent = node.parent
		if parent and parent.k > k:
			self.cut(node, parent)
			self.cascade(parent)
		if self.min.k > k:
			self.min = node

	def cut(self, node, parent):
		self.removeChild(node, parent)
		parent.degree -= 1
		self.root(node)
		node.mark = False

	def cascade(self, node):
		parent = node.parent
		if parent:
			if parent.mark:
				self.cut(node, parent)
				self.cascade(parent)
			else:
				parent.mark = True

	def remove(self, node):
		self.decreaseKey(node, float('-inf'))
		self.Dequeue()



class ABFibHeap(object):
	def __init__(self):
		self.A = FibHeap()
		self.B = FibHeap()
		self.T = FibHeap()
		self.time = 0

	def __len__(self):
		return len(self.A)

	def Count(self):
		return len(self)

	def Clear(self):
		self.A.Clear()
		self.B.Clear()

	def  __bool__(self):
		return bool(self.A)

	def Enqueue(self, v, kA, kB):
		self.time += 1
		nA = self.A.Enqueue(kA, v)
		nB = self.B.Enqueue(kB, v)
		nA.sibling, nB.sibling = nB, nA
		nT = self.T.Enqueue(self.time, (nA, nB))
		nA.timer, nB.timer = nT, nT

	def DequeueA(self):
		nA = self.A.Dequeue()
		nB = nA.sibling
		self.B.remove(nB)
		self.T.remove(nA.timer)
		return nA.v

	def DequeueB(self):
		nB = self.B.Dequeue()
		nA = nB.sibling
		self.A.remove(nA)
		self.T.remove(nB.timer)
		return nB.v

	def DequeueLast(self):
		nA, nB = self.T.Dequeue().v
		self.A.remove(nA)
		self.B.remove(nB)
		return nA.v


heap = ABFibHeap()


heap.Enqueue('E', 50.0, 32.9)
heap.Enqueue('F', 14.0, 5.0)
heap.Enqueue('A', 7.0, 1.0)
heap.Enqueue('D', 2.0, 5.0)
heap.Enqueue('C', 0.3, 5.0)
heap.Enqueue('B', 9.4, 2.0)

print(heap.DequeueB())
print(heap.DequeueB())
print(heap.DequeueA())
print(heap.DequeueA())
print(heap.DequeueLast())
print(heap.DequeueB())


for i in range(30):
	heap.Enqueue(i, i, -i)

while heap:
	print(heap.DequeueA() + heap.DequeueB())
