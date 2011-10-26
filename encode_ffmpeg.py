import sys, getopt, re
from subprocess import Popen, PIPE, STDOUT

opts = getopt.getopt( sys.argv[1:], 'p:t:s:b:', ['path', 'target', 'size', 'bitrate'] )

#print 'Opts:', opts
path = opts[0][0][1]
target = opts[0][1][1]
size = opts[0][2][1]
bitrate = opts[0][3][1]

print path, target, bitrate

path_to_target = '%s%s' % ( path, target )
extension_re = re.compile( '\..+$' )
result_file = extension_re.sub( '.mp4', target ) 
path_to_result = '%s%s' % ( path, result_file )
print path_to_target, path_to_result

cmd = '/usr/local/bin/ffmpeg -i %s -y -an -s %s -vcodec libx264 -r 24 -b %sk -qcomp 1 -b_strategy 2 -subq 7 %s' % ( path_to_target, size, bitrate, path_to_result )
print cmd
ffmpeg_stdout = Popen( cmd, shell=True, stdout=PIPE, stderr=STDOUT )
ffmpeg_result = ffmpeg_stdout.communicate()[0]
print ffmpeg_result
print '<AS3><resultFile>' + result_file + '</resultFile></AS3>'
