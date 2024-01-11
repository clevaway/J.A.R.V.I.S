import subprocess


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
            subprocess.run(["say", text])
        except Exception as e:
            print(f"Error during text-to-speech: {e}")
            # Add an indented block of code here if needed
