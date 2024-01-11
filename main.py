from modules.speech_to_text import SpeechToText
from modules.text_to_speech import TextToSpeech
from modules.ollama_nlp import OllamaNLP
# from modules.command_executor import CommandExecutor
# from config.config import Config


def main():
    # Initialize modules
    speech_to_text = SpeechToText()
    text_to_speech = TextToSpeech()
    ollam_nlp = OllamaNLP()
    # command_executor = CommandExecutor()

    # Load configuration
    # config = Config()

    while True:
        # Listen for user input
        user_input = speech_to_text.listen()

        # Process user input using NLP
        processed_input = ollam_nlp.generate_text("llama2", user_input)

        # # Execute command based on processed input
        # response = command_executor.execute(processed_input)

        print(processed_input)
        # Convert response to speech
        text_to_speech.speak(processed_input)


if __name__ == "__main__":
    main()
