from subprocess import Popen, PIPE, STDOUT

gitbrew = Popen( '/usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"', shell=True )
gitbrew_result = gitbrew.communicate()[0]
print '<AS3>Installing homebrew...</AS3>'
print gitbrew_result

ffmpeg = Popen( '/usr/local/bin/brew install --use-gcc ffmpeg', shell=True, stdout=PIPE )
ffmpeg_result = ffmpeg.communicate()[0]
print '<AS3>Installing ffmpeg...</AS3>'
print ffmpeg_result
print '<AS3>Done!</AS3>'
