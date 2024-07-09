import os
import time
from dotenv import load_dotenv
import speech_recognition as sr
from elevenlabs.client import ElevenLabs
from elevenlabs import generate, save
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play_audio

load_dotenv(override=True)

ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

class Interlocus:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.tts_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        self.audio_file = "tts_output.mp3"  # Audio file to save TTS output

    def speak(self, text):
        audio = generate(
            api_key=ELEVENLABS_API_KEY,
            text=text,
            voice="xFjhlCVIoEAjDeZpAmFe",
            model="eleven_turbo_v2",
        )

        save(audio, self.audio_file)  # Save audio to file
        audio_segment = AudioSegment.from_file(self.audio_file, format="mp3")
        
        play_process = play_audio(audio_segment)

        while play_process.is_playing():
            if self.is_speaking():
                play_process.stop()
                print("Stopped playback due to detected speech.")
                break
            time.sleep(0.1)  # Brief sleep to prevent high CPU usage

    def is_speaking(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening for speech to stop TTS...")
            try:
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=1)
                if audio:
                    print("Speech detected.")
                    return True
            except sr.WaitTimeoutError:
                return False
            except sr.UnknownValueError:
                return False
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return False
        return False

    def listen(self):
        with self.microphone as source:
            print("Listening for speech...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source)
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized speech: {text}")
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

# Example usage
# interlocus = Interlocus()
# interlocus.speak("Hello, this is a test.")
# interlocus.listen()
# interlocus.speak("Let's try speaking again.")
# interlocus.listen()