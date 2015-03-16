#Nim 10.2
import strutils
var 
  relation = readLine(stdin)
  val = parseInt(readLine(stdin))
  n = parseInt(readLine(stdin))
  
for i in 0 .. n:
  echo("Term ", i, ": ", val)
  for r in relation.split():
    case r[0]:
      of '+': val += parseInt(r[1.. -1])
      of '-': val -= parseInt(r[1.. -1])
      of '*': val *= parseInt(r[1.. -1])
      of '/': val = val div parseInt(r[1.. -1])
      else:
        echo("Unrecognised Command")