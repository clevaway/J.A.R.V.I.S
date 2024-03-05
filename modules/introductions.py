import os
import multiprocessing
from moviepy.editor import VideoFileClip
from modules.text_to_speech import TextToSpeech

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

text_to_speech = TextToSpeech()


def play_video():
    # intro video:
    # Construct the path to the video file
    video_path = os.path.join(
        script_dir, '..', 'assets', 'videos', 'welcome_hud.mp4')

    clip = VideoFileClip(video_path)
    # Set the new height and width
    clip_resized = clip.resize(height=720, width=1280)
    # Reduce the volume of the clip by 50%
    clip_resized = clip_resized.volumex(0.5)

    clip_resized.preview()


def speak_introduction():
    # introductions
    text_to_speech.speak("Allow me to introduce myself. I am Jarvis, a virtual artificial intelligence assistant. Importing all preferences from home interface. calibrating all systems. Please stand by. systems are now fully operational.")


def run_introduction():
    # Create threads
    t1 = multiprocessing.Process(target=speak_introduction)
    t2 = multiprocessing.Process(target=play_video)

    # Start threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()
