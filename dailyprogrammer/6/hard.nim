import future, math, strutils

proc nimerize(heaps: var seq[int]): seq[int] =
  var acc = 0
  for h in heaps:
    acc = h xor acc
  for i in heaps.low ..heaps.high:
    if (acc xor heaps[i]) < heaps[i]:
      heaps[i] = acc xor heaps[i]
      return heaps
  return @[]

var heap = map(readLine(stdin).split, parseInt)

echo heap

while heap.nimerize.len != 0:
  echo heap
  if sum(heap) == 0:
    quit "I WIN!"
  var 
    re = readLine(stdin)
    i = parseInt(re.split[0])
    n = parseInt(re.split[1])
  heap[i] -= n

quit "I GIVE UP!"
