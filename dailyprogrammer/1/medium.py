#Way too big for what it does, pickle is nice though

import re
import sys
import pickle

events = []
options = {'savefile':'plan'}

def showOptions(match):
	for entry in options:
		print(entry, ":", options[entry])

def setOption(match):
	global options
	k, v = match.group(1), match.group(2)
	if k in options:
		options[k] = v
	else:
		print("Bad option")

def show(match):
	for e in events:
		print('{:<5}{:<20}'.format(*e))

def add(match):
	global events
	hour = int(match.group(1))
	name = match.group(2)
	if not 0 <= hour <= 24:
		print("Bad hour")
	elif len([0 for (_, n) in events if n == name]) != 0:
		print("Name clash")
	else:
		events.append((hour, name))

def load(match):
	global options, events
	fname = match.group(1)
	with open(fname, 'rb') as f:
		events, options = pickle.load(f)		

def exit(match):
	with open(options['savefile'], 'wb') as f:
		pickle.dump((events, options), f)
	sys.exit(0)

def remove(match):
	global events
	events = [(h, n) for h,n in events if not n == match.group(1)]

def edit(match):
	global events
	orig = match.group(1)	
	hour = int(match.group(2))
	name = match.group(3)
	events = [(h, n) for h,n in events if not n == orig]
	if not 0 <= hour <= 24:
		print("Bad hour")
	elif len([0 for (_, n) in events if n == name]) != 0:
		print("Name clash")
	else:
		events.append((hour, name))
		


commands = {r'add ([0-9]{1,2}) ([a-zA-Z]+)' : add,
			r'remove ([a-zA-Z]+)' : add,
			r'edit ([a-zA-Z]+) ([0-9]{1,2}) ([a-zA-Z]+)': edit,
			r'load ([a-zA-Z]+)':load,
			r'options': showOptions,
			r'set-option ([a-zA-Z]+) ([a-zA-Z]+)': setOption,
			r'show': show,
			r'exit': exit}

while(True):
	line = input("Command?\n")
	for command in commands:
		match = re.match(command, line)
		if match:
			commands[command](match)
			break
	else:
		print('Unknown command')
		for command in commands:
			print(command)
