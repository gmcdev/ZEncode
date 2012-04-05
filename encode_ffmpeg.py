import sys, getopt, re
from subprocess import Popen, PIPE, STDOUT

opts = getopt.getopt( sys.argv[1:], 'f', ['ffmpegcmd'] )
try:
	cmd = opts[1][0]
except:
	print '-f (--ffmpegcmd) must be specified with a valid ffmpeg command' 
	sys.exit( 2 )

print 'encode_ffmpeg.py -f '
print cmd[1:-1] + '\n'
ffmpeg_stdout = Popen( cmd[1:-1], shell=True, stdout=PIPE, stderr=STDOUT )
ffmpeg_result = ffmpeg_stdout.communicate()[0]
print ffmpeg_result
