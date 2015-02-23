#Testing framework
#Note: Not unit test. All of the scripts are self-contained. Testing is done only on stdin/stdout interaction, not side effects. Just simply sanity checks and example usages.
import subprocess
from testset import tests

def runCmd(s):
	return subprocess.call(['D:\\Program Files (x86)\\Git\\bin\\bash.exe', '-c', s]) #WHYYYYY!

corrects = 0

runCmd('rm -rf results') #Dangerous?
for n, spec, testset in tests:
	runCmd('mkdir -p results/{0}/{1}'.format(n, spec))
	for test in testset:
		runCmd('cat input/{0}/{1}/{2}.txt | (cd {0}; py {1}.py > ../results/{0}/{1}/{2}.txt)'.format(n, spec, test))
		if runCmd('diff results/{0}/{1}/{2}.txt output/{0}/{1}/{2}.txt'.format(n, spec, test)):
			print('{}/{} - {}'.format(n, spec, test), 'FAIL!')
			break
		else:
			print('{}/{} - {}'.format(n, spec, test), 'pass')
	else:
		corrects += 1

print('{}/{}'.format(corrects, len(tests)), 'challenges tested and passed!')

