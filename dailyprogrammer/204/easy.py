#Meh, long code, not as elegant as I would like
import re

with open('macbeth.txt') as f:
	content =  f.readlines()

regex = re.compile(input()) #Get the line for searching

actregex = re.compile('ACT.*')
sceneregex = re.compile('SCENE.*')
paragraphs = []
buff, characters, scene, act, speaker = '', set(), '', '', '' #Keep track of the containing information

for line in content: #Handle lines one by one
	if actregex.match(line): #It's an act!
		act = line.split('.')[0]
	if sceneregex.match(line): #It's a scene!
		scene = line.split('.')[0]
		characters = set()
	if line[0:4] == '    ': #No, it's line!
		buff += line	
	elif line[0:2] == '  ': #Speaker
		speaker = line[2:].split('.')[0]
		characters.add(speaker) #Note, the characters map is shared between multiple paragraphs
	elif not buff == '': #If there's lines to flush, do it, not, we do not flush by speaker, since they follow an empty line
		paragraphs.append((buff, act, scene, characters, speaker))
		buff = ''

for p in paragraphs:
	if regex.search(p[0]): #The paragraph contains the line
		paragraph, act, scene, characters, speaker = p
		print(act)
		print(scene)
		print('Characters in scene: ' + ', '.join(characters))
		print('Spoken by: ' + speaker)
		print(paragraph.encode('cp437', 'replace').decode('cp437')) #Windows terminals don't like characters