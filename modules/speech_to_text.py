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
