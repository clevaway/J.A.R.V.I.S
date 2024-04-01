from modules.speech_to_text import SpeechToText
from modules.text_to_speech import TextToSpeech
from modules.ollama_nlp import OllamaNLP
from modules.introductions import run_introduction
# from modules.command_executor import CommandExecutor
# from config.config import Config

# importing vibranium modules
from modules.vibranium.dateAndtime.time import CurrentTimeTeller
from modules.vibranium.dateAndtime.date import CurrentDateTeller
from modules.vibranium.online_ops.index import OnlineOps


def main():
    # Initialize modules
    speech_to_text = SpeechToText()
    text_to_speech = TextToSpeech()
    ollam_nlp = OllamaNLP()

    # init vibranium modules
    time_teller = CurrentTimeTeller()
    date_teller = CurrentDateTeller()
    online_ops = OnlineOps()
    # command_executor = CommandExecutor()

    # Load configuration
    # config = Config()
    # run intro
    # run_introduction()

    while True:
        # Listen for user input
        user_input = speech_to_text.listen()

        # Check if command is 'time'
        if 'time' in user_input:
            print("Time requested")
            response = time_teller.tell_time()
            processed_results = ollam_nlp.generate_text(
                "jarvis:latest", user_input, "For some context for you. it is " + response)
            text_to_speech.speak(processed_results)
            continue

        keywords = ['date', 'today', 'month', 'year']
        if any(keyword in user_input for keyword in keywords):
            print("Date requested")
            response = date_teller.tell_date()
            processed_results = ollam_nlp.generate_text(
                "jarvis:latest", user_input, "For some context for you. it is " + response)
            text_to_speech.speak(processed_results)
            continue
        # if "wikipedia" in user_input:
        #     print("Wikipedia requested")

        #     # Split the user input by 'wikipedia'
        #     parts_after_wikipedia = user_input.split('wikipedia', 1)

        #     if len(parts_after_wikipedia) > 1:
        #         # Split the second part by spaces and join the words starting from the second word
        #         search_keyword = ' '.join(parts_after_wikipedia[1].split()[1:])
        #         response = online_ops.search_wikipedia(search_keyword)
        #         text_to_speech.speak(response)
        #     continue
        # Check if command is 'search'
        if 'search' in user_input:
            print("Search requested")

            # Split the user input by 'search'
            parts_after_search = user_input.split('search', 1)

            if len(parts_after_search) > 1:
                # Split the second part by spaces and join the words starting from the second word
                search_keyword = ' '.join(parts_after_search[1].split()[1:])
                online_ops.search_google(search_keyword)
                text_to_speech.speak("Coming up, one second")
            continue
        if 'play' in user_input:
            print("Youtube requested")
            parts_after_youtube = user_input.split('play', 1)
            if len(parts_after_youtube) > 1:
                # Extract the video title
                video = ' '.join(parts_after_youtube[1].split())
                online_ops.play_on_youtube(video)
                text_to_speech.speak("Playing on youtube.")
            continue

        # Process user input using NLP
        processed_input = ollam_nlp.generate_text("jarvis:latest", user_input)

        # # Execute command based on processed input
        # response = command_executor.execute(processed_input)

        # print(processed_input)
        # Convert response to speech
        text_to_speech.speak(processed_input)


if __name__ == "__main__":
    main()
