from subprocess import Popen, PIPE, STDOUT

gitbrew = Popen( 'curl -L https://github.com/mxcl/homebrew/tarball/master | tar xz --strip 1 -C /usr/local/', shell=True )
gitbrew_result = gitbrew.communicate()[0]
print '<AS3>Installed homebrew.</AS3>'
print gitbrew_result

ffmpeg = Popen( '/usr/local/bin/brew install --use-gcc ffmpeg', shell=True, stdout=PIPE )
ffmpeg_result = ffmpeg.communicate()[0]
print '<AS3>Installed ffmpeg.</AS3>'
print ffmpeg_result
