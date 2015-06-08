#I find nim to be strange and unpredictable

import tables, future, sequtils, strutils, algorithm

var
    lookup = {'0':'0', '1':'1', '2':'5', '3':'X', '4':'X', '5':'2', '6':'9', '7':'X', '8':'8', '9':'6'}.toTable
    start = 1962
    count = 0

#Luckily we can do this quite simply, I fear for performance though
proc upside(i: int): bool = #I hate type specs
    var
        ss = toSeq(items($i))
    return ss == ss.reversed.mapIt(char, lookup[it]) #I should not have to specify char here, it makes little sense

while not start.upside:
    inc start

echo start

for i in 0..10000:
    if i.upside:
        inc count 

echo count