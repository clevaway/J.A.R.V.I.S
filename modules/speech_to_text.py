import os
import subprocess
import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                # Adjust for ambient noise and listen for user input
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5)

                # Convert audio to text
                text = self.recognizer.recognize_google(audio)
                print("You said:", text.lower())
                return text.lower()

            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
                return "Hey there"
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")
                return ""
    # def listen(self):
    #     try:
    #         print("C Command running...")
    #         # go to the parent directory using subprocess
    #         subprocess.run(
    #             ['cd', '..'],
    #             capture_output=True,  # Python >= 3.7 only
    #             text=True  # Python >= 3.7 only
    #         )
    #         subprocess.run(
    #             ['cd', 'whisper.cpp'],
    #             capture_output=True,  # Python >= 3.7 only
    #             text=True  # Python >= 3.7 only
    #         )

    #         result = subprocess.run(
    #             ["./command", "-m", "./models/ggml-small.bin", "-t", "8"],
    #             stdout=subprocess.PIPE,
    #             universal_newlines=True  # Python >= 3.7 also accepts "text=True"
    #         )
    #         print(result.stdout)

    #         # # run the C++ command and get the output
    #         # result = subprocess.run(["./command", "-m", "./models/ggml-small.bin", "-t", "8"],
    #         #                         cwd="./modules/whisper.cpp", capture_output=True, text=True)
    #         # print(result)
    #         # # print the combined output of stdout and stderr
    #         # print(result.stdout.decode())

    #         # # extract the text from the output
    #         # text = result.stdout.strip()
    #         # print("You said:", text.lower())
    #         # return text.lower()

    #     except subprocess.CalledProcessError as e:
    #         print(f"Error running command: {e}")
    #         return ""
