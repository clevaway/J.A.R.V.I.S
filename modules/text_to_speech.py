# import subprocess
import os
import subprocess
from elevenlabs.client import ElevenLabs
from elevenlabs import generate, play
from dotenv import load_dotenv

load_dotenv()

# ELEVEN_API_KEY = os.getenv('ELEVEN_API_KEY')


class TextToSpeech:
    def __init__(self):
        # Initialize text-to-speech engine
        # Use macOS built-in tools or a third-party library here
        pass

    def speak(self, text):
        # Convert text to speech and play it
        # Use the initialized text-to-speech engine
        try:
            # Using the macOS 'say' command to speak the text with the system's default voice
            print("Saying: ", text)
            subprocess.run(["say", text])
        except Exception as e:
            print(f"Error during text-to-speech: {e}")
            # Add an indented block of code here if needed
        # try:
        #     # Using the macOS 'say' command to speak the text with the system's default voice
        #     print("Saying: ", text)
        #     # models = client.models.get_all()
        #     # print(models)
        #     audio = generate(
        #         # api_key="YOUR_API_KEY", (Defaults to os.getenv(ELEVEN_API_KEY))
        #         api_key=ELEVEN_API_KEY,
        #         text=text,
        #         voice="Daniel",
        #         model="eleven_turbo_v2",
        #     )

        #     play(audio)
        # except Exception as e:
        #     print(f"Error during text-to-speech: {e}")
        #     # Add an indented block of code here if needed
