import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

import sounddevice as sd
from kokoro_onnx import Kokoro
import asyncio


load_dotenv(override=True)

KOKORO_VOICE = os.getenv('KOKORO_VOICE')


class Interlocus:
    def __init__(self):
        self.kokoro = Kokoro("kokoro-v0_19.onnx", "voices-v1.0.bin")
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    async def speak(self, text):
        print(f"JARVIS: {text}")
        
        stream = self.kokoro.create_stream(
            text,
            voice=KOKORO_VOICE,
            speed=1.0,
            lang="en-us",
        )

        count = 0
        async for samples, sample_rate in stream:
            count += 1
            print(f"Speaking ({count})...")
            sd.play(samples, sample_rate)
            sd.wait()

    def listen(self):
        with self.microphone as source:
            print("SYSTEM: Listening...")
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


# -------
# The eleven labs integration below, and the local tts inegration code above
# -------

# import os
# from dotenv import load_dotenv
# import speech_recognition as sr
# from elevenlabs.client import ElevenLabs
# from elevenlabs import generate, play
# from dotenv import load_dotenv


# load_dotenv(override=True)

# ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
# ELEVENLABS_VOICE_ID = os.getenv('ELEVENLABS_VOICE_ID')

# class Interlocus:
#     def __init__(self):
#         self.tts_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
#         self.recognizer = sr.Recognizer()
#         self.microphone = sr.Microphone()

#     def speak(self, text):
#         print(f"JARVIS: {text}")
#         # Generate audio and play directly
#         audio = generate(
#             api_key=ELEVENLABS_API_KEY,
#             text=text,
#             voice=ELEVENLABS_VOICE_ID,
#             model="eleven_turbo_v2",
#         )
#         play(audio)

#     def listen(self):
#         with self.microphone as source:
#             print("SYSTEM: You can speak...")
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