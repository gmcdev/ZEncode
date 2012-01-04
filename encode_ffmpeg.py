import sys, getopt, re
from subprocess import Popen, PIPE, STDOUT

print 'encode_ffmpeg.py -f '
opts = getopt.getopt( sys.argv[1:], 'f', ['ffmpegcmd'] )
#print 'Opts:', opts
#cmd = '/usr/local/bin/ffmpeg -i %s -y %s -s %s -vcodec libx264 -r 24 -b %sk -qcomp 1 -b_strategy 2 -subq 7 %s' % ( path_to_target, audio, size, bitrate, path_to_result )
try:
	cmd = opts[1][0]
except:
	print '-f (--ffmpegcmd) must be specified with a valid ffmpeg command' 
	sys.exit( 2 )

print cmd[1:-1] + '\n'
ffmpeg_stdout = Popen( cmd[1:-1], shell=True, stdout=PIPE, stderr=STDOUT )
ffmpeg_result = ffmpeg_stdout.communicate()[0]
print ffmpeg_result
