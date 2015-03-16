#nim 10.2
import strutils, tables, future
var 
  relation = readLine(stdin)
  val = parseInt(readLine(stdin))
  n = parseInt(readLine(stdin))

template TL (op:expr): expr {.immediate} =
  (x :int, y :int) => op(x, y)
var lookup = {'+': `+`.TL, '-': `-`.TL, '*': `*`.TL, '/': `div`.TL }.toTable

for i in 0 .. n:
  echo("Term ", i, ": ", val)
  for r in relation.split():
    val = lookup[r[0]](val, parseInt(r[1 .. -1]))