import sys, getopt, re
from subprocess import Popen, PIPE, STDOUT

opts = getopt.getopt( sys.argv[1:], 'f', ['file'] )
try: 
	file = opts[1][0]
except: 
	print '-f (--file) must be specified with a valid file path'
	sys.exit( 2 )

stdout = Popen( '/usr/local/bin/ffmpeg -i '+file, shell=True, stdout=PIPE, stderr=STDOUT )
result = stdout.communicate()
print result[0]
