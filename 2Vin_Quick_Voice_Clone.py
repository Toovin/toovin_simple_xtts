import os
import pygame
from TTS.api import TTS ## THIS WILL LOOK LIKE ITS ERRORED. ITS NOT. ITS LYING.
# Make sure you're in the environment you installled TTS in. rrrrrRRRRRRREEEEEEEEEEEEEEE.
# This python spell scroll contains annotations of the magics and its inner workings. Be wise, be well.
# EXTREEEEEEEEEEEME!
# Function to play sound
def play_sound(sound_path):
    if os.path.exists(sound_path):  # Check if the sound file exists
        pygame.mixer.init() # mixit init - sounds within it!
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)  # Wait and let the sound play. Adjust the tick rate as necessary. Whats the tick rate for?
    else:
        print("WHY YOU NO LIKE SOUNDS? YOU CAN SET DINGS AND ERROR NOISES!!! REEEEEEEEEEE!!")

#BELLS AND WHISTLES, WOOOOOOOOOO! Optional. Set them, or get yelled at.
finished_sound_file= "x:/path/your_ding.mp3" #This NEEDS the full path, including file extension. Tested/usable so far are mp3/wav. This is nice if you walk away to let it process.
error_sound_file= "x:/path/your_error.mp3" #This NEEDS the full path, including file extension. Tested/usable so far are mp3/wav. This is nice if you like disapointing sounds.

#SECTIONES DE IMPORTANTE audio settings
render_outfile= "x:/path/your_CLONED_NEW_render.mp3" #This is the FULL PATH+FILENAME.EXTENSION(MP3/WAV). Example: C:/Dogebonk/Bonky_message.mp3
audio_out_dir=os.path.dirname(render_outfile)  # Extract the directory path from the full path. Used to check if we need to make a folder or not for new output. How Convenient!
speaker_wav_path= "x:/path/your_speaker_sample.mp3" #This is the file, at least 3 seconds, that has the voice SOURCE/SAMPLE recording. Quality / clarity matters!

# Create output directory if it doesn't exist. Like. C:/Dogebonk/Totally/New/Folder/for/that/audio/out/put/directory/file.mp3
os.makedirs(audio_out_dir, exist_ok=True)

# Text to synthesize. TYPE THE STUFF HERE. TYPE ALL THE THINGS HERE. IT GOES DOWN INTO : tts.tts_to_file(text=text_to_synth,
text_to_synth = "Oh, why hello there! I used to be an adventurer like you, until I took an arrow to the knee."
# I'm sure with some creativity, you can learn how to manipulate ways to input text from other things, like, an LLM. Or some psedeo random speech generator function.

# Check if required paths exist. This is for the VOICE SAMPLE you are cloning FROM.
paths_to_check = [speaker_wav_path]
for path in paths_to_check:
    if not os.path.exists(path):
        play_sound(error_sound_file)
        print(f"Error: The path {path} does not exist.")
        exit()

# TTS generation. THE MAGICAL SETTINGS ARE HERE. YOU NEED i dunno 6 gigs vram? im on 8gb and it works fine. maybe 4gb works. 
try:
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v1") ## Uh. Im not sure what this is referencing. Run this script from at least 1 folder (from x:/dir/TTS/) deep max .
    # Either way, that tts = thing, it definitely references the xtts_v1 model. So, you can probably change things (the model) up here if you so choose. Below parameters may not be compatible with this script if you attempt.
    # LOOKY HERE VVVVVV
    tts.to(0) # HEY THIS ONE IS IMPORTANT, LOOK AT ME. IF YOU HAVE NO GPU, TYPE WITH QUOTES "cpu". (0) = gpu 1. Cant use multi, but you can change that 0 to 1. Or 2. Good luck. CPU ENABLE IS      tts.to("cpu") 
    # LOOKY HERE ^^^^^^
    tts.tts_to_file(text=text_to_synth,
                    file_path=str(render_outfile),
                    speaker_wav=str(speaker_wav_path),
                    decoder_iterations=30, #Normal is like 30. above 250 seems fruitless.
                    language="en",
                    temperature=0.55, #This is like.. uh.. imagine Trump talking. Taking pauses. For effect. And the higher value removes that.
                    diffusion_temperature=0.55, #Almost same thing as above? But pitch wise? like, a more droning (0.1) to crazy (1.0). Possibly works above 1.
                    # length_penalty=2, #How terse is the output? normall is 2? i think? or 1? Dunno, good luck.
                    # repetition_penalty=1, # Uhhhh, mmmmmmm?
                    # do_sample=True, # Do we use a sample voice file? YES!
                    cond_free_k=2, #Higher = tries hard to make voice match? Dunno, default is "2". Wierd chorus wobbly sound if too high.
                    # gpt_cond_len=120, #Eeeeh dont need this. Determines legnth of audio to use from sample.
                    top_p=.8,
                    top_k=80) # This can go pretty high. 250 has great output. 40 is the actual default.
    play_sound(finished_sound_file)
    print("Ok, Done! Good luck!")

except Exception as e:
    play_sound(error_sound_file)
    print(f"HOLY BONK, TAKE A LOOK AT THIS MESS: {e}")
