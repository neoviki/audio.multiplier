## AUDIO LOOPER

This script is used to multiply(loop) the length of existing ".mp3" audio file to the specified target length.


#### USAGE

  $python audio_multiplier.py <input mp3 file name> <expected target length>

  New file will be stored with prefix enlarged_<input_mp3_file>.mp3

#### Dependencies 

    - pydub  ( pip install pydub )
    - ffmpeg ( brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora )
