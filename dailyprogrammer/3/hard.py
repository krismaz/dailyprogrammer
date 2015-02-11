#Scrabble-bot lookup of glory.

#This solution uses a lookup-table built from the wordlist, where the keys are the sorted characters, making lookups very fast, but pre-processing rather heavy.

with open('wordlist.txt', errors='ignore') as f:
    content = f.readlines()

lookup =  {''.join(sorted(i.strip().lower())) : i.strip().lower() for i in content}
log = []

while True:
	try:
		query = input()
		log.append(lookup[''.join(sorted(query.lower()))])
	except:
		break

for s in sorted(log, key = len):
	print(s)