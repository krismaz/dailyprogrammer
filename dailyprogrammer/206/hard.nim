import strutils, tables, future

proc pop[T](s: var seq[T]) : T =
  var 
    r = s[s.len-1]
  s.delete(s.len-1)
  r

template r(s: expr, op: (int,int)->int): expr =
  var
    t = s.pop
  s.add op(s.pop, t)

proc rpn(exp: string, lookup: Table[int, int] , index: int): int =
  var 
    stack = newSeq[int] 0
  for s in exp.split():
    case s[0]:
      of '+': r(stack, `+`)
      of '-': r(stack, `-`)
      of '*': r(stack, `*`)
      of '/': r(stack, `div`)
      of '(':
        var
          lId = index - s[1 .. -2].parseInt
        if lookup.hasKey lID:
          stack.add lookup[lId]
        else:
          raise newException(IndexError, "Hai")
      else:
        stack.add s.parseInt
  stack[0]

var
   exp = stdin.readLine
   n = -1
   lookup = initTable[int, int] (32)


while true:
  var
    s = stdin.readLine
  if s.find(':') != -1:
    lookup[s.split(':')[0].parseInt] = s.split(':')[1].parseInt
  else:
    n = s.parseInt
    break

for i in 0 .. n:
  if lookup.hasKey i:
    echo i, " : ", lookup[i]
  else:
    try:
      var 
        val = rpn(exp, lookup, i)
      echo i, " : ", val
      lookup[i] = val
    except:
      discard