import strutils, sequtils, tables, future

template len(slice: Slice): expr =
  var count = 0
  for c in slice:
    count += 1
  count

template toSeq(slice: Slice, typed: typedesc): expr =
  block:
    var 
      res = newSeq[typed](len(slice))
      counter = 0
    for i in slice:
      res[counter] = i
      counter += 1
    res  

proc `*`(s: string, i: int): string =
  var buff = ""
  for c in 1 .. i:
    buff &= s
  buff

const
  chars = toSeq('a'..'z', char)
var
  lookup = zip(".-,-...,-.-.,-..,.,..-.,--.,....,..,.---,-.-,.-..,--,-.,---,.--.,--.-,.-.,...,-,..-,...-,.--,-..-,-.--,--..".split(","), chars).toTable
  revlookup = zip(chars, ".-,-...,-.-.,-..,.,..-.,--.,....,..,.---,-.-,.-..,--,-.,---,.--.,--.-,.-.,...,-,..-,...-,.--,-..-,-.--,--..".split(",")).toTable

proc decode(codes: seq[string]): void =
  for code in codes:
    for morse in code.split:
      write(stdout, lookup[morse])
  write(stdout, " ")

proc encode(input: string): void =
  for c in input:
      write(stdout, revlookup[c])
  write(stdout, " ")


var input = readLine(stdin)

for w in input.split(" / "):
  w.split.decode