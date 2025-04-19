#This software needs pydub, Install before executing the program
#pip install pydub
#brew install ffmpeg --with-libvorbis --with-sdl2 --with-theora
#This software will give a enlarged mp3 file not more than expected_length
import sys
from pathlib import Path
from pydub import AudioSegment

def main():
    if len(sys.argv) < 3:
        print("USAGE: python audio.multiplier.py <mp3 file name> <repeat_count>")
        exit(0)

    sound_file = sys.argv[1]
    if not sound_file.endswith('.mp3'):
        print("Unrecognized extension, This software only supports .mp3 extension")
        exit(0)

    repeat_count = sys.argv[2]
    if not repeat_count.isdigit():
        print("Expected length has to be an integer")
        exit(0)

    repeat_count = int(repeat_count)

    audio = AudioSegment.from_mp3(sound_file)
    audio_len = len(audio) / (1000) # convert milliseconds to seconds
    print(f"Existing audio length : {audio_len} seconds")

    multiplied_audio = audio
    print(f"\tx {1}")
    # Concatenation is just adding
    for i in range(repeat_count-1):
        print(f"\tx {i+2}")
        multiplied_audio += audio

    new_audio_len = len(multiplied_audio) / (1000) # convert milliseconds to seconds
    print(f"New audio length : {new_audio_len} seconds")

    file_path = Path(sound_file)
    infile      = file_path.stem       # filename without extension
    infile_extn = file_path.suffix     # .mp3

    output_file = f"{infile}_x{repeat_count}{infile_extn}"
    # writing mp3 files is a one liner
    multiplied_audio.export(output_file, format="mp3")
    print(f"Output Audio File : {output_file}")

if __name__ == "__main__":
    main()
