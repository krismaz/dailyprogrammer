#Nim 0.10.2
import strutils, tables, sets, queues, sequtils, future
var
    ab = stdin.readLine.split.map parseInt
    lookup = initTable[string, HashSet[string]](32)

proc tablerize(doc: string):  void =
    var
        preproc = doc[doc.low .. doc.find("(")-1].replace("&").split(",") #Input processing
        preproc2 = preproc.distribute(preproc.len div 2).map((s: seq[string]) => s.foldr(a & "," & b).strip) #Even more input processing
    for author in preproc2:
        for author2 in preproc2:
            if not lookup.hasKey author:
                lookup[author] = initSet[string]()
            lookup.mget(author).incl author2 # [] doesn't work, brilliant

proc ErdosNumber(dude: string): int = #BFS
    var
        todo = initQueue[tuple[a: string, b: int]](32)
        done = initSet[string]()
    todo.enqueue ((dude, 0))
    while todo.len > 0:
        var 
            (author, dist) = todo.dequeue
        if not done.contains author:
            done.incl author
            if author == r"Erdös, P.":
                return dist
            for author2 in lookup[author]:
                todo.enqueue ((author2, dist+1))
    return -1

            
for i in 1 .. ab[0]:
    stdin.readLine.tablerize

for i in 1 .. ab[1]:
    var
        author = stdin.readLine
    echo author, " ", author.ErdosNumber