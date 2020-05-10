#This software needs pydub, Install before executing the program 
#pip install pydub
#brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora
#This software will give a enlarged mp3 file not more than expected_length
import sys
from pydub import AudioSegment

def main():
    if len(sys.argv) < 3:
        print "USAGE: python audio_multiplier.py <mp3 file name> <expected_audio_length in minutes>"
        exit(0)

    sound_file = sys.argv[1] 
    if not sound_file.endswith('.mp3'):
        print "Unrecognized extension, This software only supports .mp3 extension"
        exit(0)

    target_length = sys.argv[2]
    if not target_length.isdigit():
        print "Expected length has to be an integer"
        exit(0)

    #Convert minutes to seconds
    target_length = int(target_length) * 60

    audio = AudioSegment.from_mp3(sound_file)
    audio_len = len(audio) / (1000) # convert milliseconds to seconds
    print "Existing audio length : ", audio_len,
    print "seconds"

    multiplied_audio = audio 
    # Concatenation is just adding
    for i in range(audio_len, target_length, audio_len):
    	multiplied_audio += audio 

    new_audio_len = len(multiplied_audio) / (1000) # convert milliseconds to seconds
    print "New audio length : ", new_audio_len,
    print "seconds"
    output_file = "enlarged_"+sound_file
    # writing mp3 files is a one liner
    multiplied_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    main()
