#Testing framework
#Note. Not unit test
import subprocess

def runCmd(s):
	return subprocess.call(['D:\\Program Files (x86)\\Git\\bin\\bash.exe', '-c', s]) #WHYYYYY!

tests = [(1, 'easy', 'A')]
corrects = 0

for n, spec, test in tests:
	runCmd('rm -rf results')
	runCmd('mkdir -p results/{0}/{1}'.format(n, spec))
	runCmd('cat input/{0}/{1}/{2}.txt | (cd {0}; py {1}.py > ../results/{0}/{1}/{2}.txt)'.format(n, spec, test))
	print()
	if runCmd('diff results/{0}/{1}/{2}.txt output/{0}/{1}/{2}.txt'.format(n, spec, test)):
		print('{}/{} - {}'.format(n, spec, test), 'FAIL!')
	else:
		corrects += 1
		print('{}/{} - {}'.format(n, spec, test), 'pass')

print('{}/{}'.format(corrects, len(tests)), 'passed!')

