#!/bin/sh
# Just copy and paste the lines below
# MAKE SURE YOU ARE HAPPY WITH WHAT IT DOES FIRST! THERE IS NO WARRANTY!

brew remove yasm
brew remove xvid
brew remove x264
brew remove theora
brew remove pkg-config
brew remove libvpx
brew remove libvorbis
brew remove libogg
brew remove lame
brew remove faac
brew remove ffmpeg

cd `brew --prefix`
git ls-files -z | pbcopy
rm -rf Cellar
bin/brew prune
pbpaste | xargs -0 rm
rm -r Library/Homebrew Library/Aliases Library/Formula Library/Contributions 
test -d Library/LinkedKegs && rm -r Library/LinkedKegs
rmdir -p bin Library share/man/man1 2> /dev/null
rm -rf .git
rm -rf ~/Library/Caches/Homebrew
