#Nim 0.10.2
import strutils, tables, re

var
    table = newOrderedTable[string, string](32)
    dna = ""

while not stdin.endOfFile:
    var 
        dataz = stdin.readline.strip.split #Congaline \o/
    try:
        var
            line = dataz[0].parseint #This throws if it's not looking at an integer
        for s in dataz[1 .. dataz.high]:
            dna &= s
    except:
        table[dataz[0]] = dataz[2].toLower

for enzyme, splitter in table:
    var
        index = dna.find splitter.replace "^" #I'd like to keep this in the table, but neste generics seems wonky 
    while index != -1: #This should really be re.findAll, but nims re module is missing indexes
        echo enzyme, " ", index+splitter.find("^"), " ", dna[max(index-5, dna.low) .. index-1],"[", splitter.replace("^", " "), "]", dna[index + splitter.len -1.. min(index + splitter.len + 11 - splitter.len, dna.high)] #Everyone loves one-liners
        index = dna.find(splitter.replace "^", index+1)