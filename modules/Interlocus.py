# import os
# from dotenv import load_dotenv
# import speech_recognition as sr
# import pyttsx3

# load_dotenv(override=True)

# class Interlocus:
#     def __init__(self):
#         self.tts_engine = pyttsx3.init()
#         self.recognizer = sr.Recognizer()
#         self.microphone = sr.Microphone()

#     def speak(self, text):
#         print(f"JARVIS: {text}")
#         self.tts_engine.say(text)
#         self.tts_engine.runAndWait()

#     def listen(self):
#         with self.microphone as source:
#             print("SYSTEM: Listening...")
#             self.recognizer.adjust_for_ambient_noise(source)
#             try:
#                 audio = self.recognizer.listen(source)
#                 text = self.recognizer.recognize_google(audio)
#                 print(f"YOU: {text}")
#                 return text
#             except sr.UnknownValueError:
#                 print("Speech Recognition could not understand audio")
#                 return None
#             except sr.RequestError as e:
#                 print(f"Could not request results from Speech Recognition service; {e}")
#                 return None


# -------
# The eleven labs integration below, and the local tts inegration code above
# -------

import os
from dotenv import load_dotenv
import speech_recognition as sr
from elevenlabs.client import ElevenLabs
from elevenlabs import generate, play
from dotenv import load_dotenv


load_dotenv(override=True)

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
ELEVENLABS_VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID')

class Interlocus:
    def __init__(self):
        self.tts_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        print(f"JARVIS: {text}")
        # Generate audio and play directly
        audio = generate(
            api_key=ELEVENLABS_API_KEY,
            text=text,
            voice=ELEVENLABS_VOICE_ID,
            model="eleven_turbo_v2",
        )
        play(audio)

    def listen(self):
        with self.microphone as source:
            print("SYSTEM: You can speak...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
                print(f"YOU: {text}")
                return text
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Speech Recognition service; {e}")
                return None