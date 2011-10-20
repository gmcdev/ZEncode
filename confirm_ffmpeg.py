from subprocess import Popen, PIPE, STDOUT

stdout = Popen( 'cd /usr/local/Cellar/ffmpeg/', shell=True, stdout=PIPE, stderr=STDOUT )
result = stdout.communicate()
print result[0]
