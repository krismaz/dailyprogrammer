#Lazy, but lazy

for i in range (99,3, -1):
	print("""{0} bottles of beer on the wall, {0} bottles of beer.
Take one down and pass it around, {1} bottle of beer on the wall.""".format(i,i-1))


#See, we could use logic and stuff, But really, this is so much easier
print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer. 
Go to the store and buy some more, 99 bottles of beer on the wall.""")