from subprocess import Popen, PIPE, STDOUT

stdout = Popen( 'cd /usr/Developer/', shell=True, stdout=PIPE, stderr=STDOUT )
result = stdout.communicate()
print result[0]
