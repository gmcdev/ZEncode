from subprocess import Popen, PIPE, STDOUT

gitbrew = Popen( '/usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"', shell=True )
gitbrew.wait()
#gitbrew_result = gitbrew.communicate()[0]
#print '<AS3>Installing homebrew...</AS3>' + gitbrew_result

lame = Popen( '/usr/local/bin/brew install lame', shell=True, stdout=PIPE )
lame.wait()
#lame_result = lame.communicate()[0]
#print '<AS3>Installing lame...</AS3>' + lame_result

yasm = Popen( '/usr/local/bin/brew install yasm', shell=True, stdout=PIPE )
yasm.wait()
#yasm_result = yasm.communicate()[0]
#print '<AS3>Installing yasm...</AS3>' + yasm_result

faac = Popen( '/usr/local/bin/brew install faac', shell=True, stdout=PIPE )
faac.wait()
#faac_result = faac.communicate()[0]
#print '<AS3>Installing faac...</AS3>' + faac_result

x264 = Popen( '/usr/local/bin/brew install --use-gcc --HEAD x264', shell=True, stdout=PIPE )
x264.wait()
#x264_result = x264.communicate()[0]
#print '<AS3>Installing x264...</AS3>' + x264_result

linkfaac = Popen( '/bin/link faac', shell=True , stdout=PIPE )
linkfaac.wait()
#linkfaac_result = linkfaac.communicate()[0]
#print '<AS3>Linking faac...</AS3>' + linkfaac_result

ffmpeg = Popen( '/usr/local/bin/brew install --use-gcc -HEAD ffmpeg', shell=True, stdout=PIPE )
ffmpeg.wait()
#ffmpeg_result = ffmpeg.communicate()[0]
#print '<AS3>Installing ffmpeg...</AS3>' + ffmpeg_result
#print '<AS3>Done!</AS3>'
