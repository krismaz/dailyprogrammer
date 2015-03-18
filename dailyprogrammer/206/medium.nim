import strutils, future, sequtils

type
  point = tuple[x,y :int]

var
  params = stdin.readLine.split.map parseInt
  h = params[0]
  w = params[1]
  r = params[2]
  plants = lc[(xc[0], y) | (y <- 0 .. h-1, xc <- stdin.readLine.pairs, xc[1] == 'x'), point]

proc dsquared(p1, p2: point): int {.inline.} =
  return (p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y)

proc pm(plants: seq[point], pa: point): int =
  proc fil(plant: point): bool {.inline.} =
    plant.dsquared(pa) <= r*r and plant != pa
  plants.filter(fil).len

echo lc[(pm(plants, (x,y)), (x,y)) | (x <- 0 .. h-1, y <-0 .. w-1), tuple[count: int, p: point]].max