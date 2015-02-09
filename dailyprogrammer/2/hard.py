#Comman line stopwatch??? Ugly yes!

from time import clock

seconds, lapped = (0, 0)
started = None
laps = []

while True:
	command = input()
	if command == 'start':
		if started == None:
			started = clock()
	elif command == 'stop':
		if started == None:
			continue
		seconds += clock() - started
		started = None
		print('{:10.2f}'.format(seconds))
	elif command == 'lap':
		lap = ((clock() - started) if not started == None else 0)  + seconds
		laps.append(lap-lapped)
		lapped = lap
	elif command == 'show':
		for i, lap in enumerate(laps):
			print('Lap {} {:10.2f}'.format(i,lap))
		print('Now {:10.2f}'.format((clock() - started) if not started == None else 0 + seconds))
	elif command == 'print':
		with open('clock.txt', 'w') as f:
			f.write('\n'.join(map(str,laps)))
	elif command == 'exit':
		break;