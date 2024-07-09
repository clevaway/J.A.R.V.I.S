from modules.vibranium.vision.vision import Vision
from modules.vibranium.online_ops.index import OnlineOps
from modules.vibranium.dateAndtime.date import CurrentDateTeller
from modules.vibranium.dateAndtime.time import CurrentTimeTeller
import os
import time
import cv2
from modules.Interlocus import Interlocus
# from modules.text_to_speech import TextToSpeech
from modules.ollama_nlp import OllamaNLP
from modules.introductions import run_introduction
from dotenv import load_dotenv

load_dotenv(override=True)

# from modules.command_executor import CommandExecutor
# from config.config import Config

# importing vibranium modules


# loading env variables
JARVIS_MODEL = os.getenv('JARVIS_MODEL')
VISION_MODEL = os.getenv('VISION_MODEL')

# print("JARVIS_MODEL => ", JARVIS_MODEL)
# print("VISION_MODEL => ", VISION_MODEL)


def main():
    # Initialize modules
    # speech_to_text = SpeechToText()
    # text_to_speech = TextToSpeech()
    interlocus = Interlocus()
    
    ollam_nlp = OllamaNLP()

    # init vibranium modules
    time_teller = CurrentTimeTeller()
    date_teller = CurrentDateTeller()
    online_ops = OnlineOps()
    vision = Vision()
    # command_executor = CommandExecutor()

    # Load configuration
    # config = Config()
    # run intro
    # run_introduction()

    while True:
        # Listen for user input
        user_input = interlocus.listen()

        # Check if command is 'time'
        if 'time' in user_input:
            print("Time requested")
            response = time_teller.tell_time()
            processed_results = ollam_nlp.generate_text(
                JARVIS_MODEL, user_input, "For some context for you. it is " + response)
            interlocus.speak(processed_results)
            continue

        keywords = ['date', 'today', 'month', 'year']
        if any(keyword in user_input for keyword in keywords):
            print("Date requested")
            response = date_teller.tell_date()
            processed_results = ollam_nlp.generate_text(
                JARVIS_MODEL, user_input, "For some context for you. it is " + response)
            interlocus.speak(processed_results)
            continue
        # if "wikipedia" in user_input:
        #     print("Wikipedia requested")

        #     # Split the user input by 'wikipedia'
        #     parts_after_wikipedia = user_input.split('wikipedia', 1)

        #     if len(parts_after_wikipedia) > 1:
        #         # Split the second part by spaces and join the words starting from the second word
        #         search_keyword = ' '.join(parts_after_wikipedia[1].split()[1:])
        #         response = online_ops.search_wikipedia(search_keyword)
        #         interlocus.speak(response)
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
                interlocus.speak("Coming up sir. one sec")
            continue
        if 'play' in user_input:
            print("Youtube requested")
            parts_after_youtube = user_input.split('play', 1)
            if len(parts_after_youtube) > 1:
                # Extract the video title
                video = ' '.join(parts_after_youtube[1].split())
                online_ops.play_on_youtube(video)
                interlocus.speak("Playing on youtube.")
            continue

        visionKeywords = ['what do you see', 'what are you looking at', 'tell me what you see',
                          'look at this', 'describe this', 'describe what you see', 'describe']
        # Check if the user wants jarvis to look at something and use the vision vibranium module
        if any(visionKeyword in user_input for visionKeyword in visionKeywords):
            # to describe what it sees
            print("Looking...")
            # Open a window and capture a photo using OpenCV
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            # cv2.imshow('Capturing', frame)
            # Wait for 3 seconds
            # time.sleep(3)
            cap.release()
            cv2.destroyAllWindows()

            # Check if the images directory exists
            images_dir = os.path.join("assets", "images")
            if not os.path.exists(images_dir):
                # If not, create it
                os.makedirs(images_dir)
            # Save the picture in the assets/images directory
            image_path = os.path.join("assets", "images", "image.jpg")
            cv2.imwrite(image_path, frame)
            print("Thinking...")
            description = vision.generate_description("llava", image_path)
            interlocus.speak(description)
            continue

        # Check if command is "go to sleep" or "goodbye", "sleep"
        goodByeKeywords = ['sleep', 'goodbye', 'go to sleep',
                           "shut down", "shutdown", "exit", "quit"]
        if any(goodByeKeyword in user_input for goodByeKeyword in goodByeKeywords):
            print("Exiting...")
            good_bye_res = ollam_nlp.generate_text(
                JARVIS_MODEL, user_input, "You always refer to me as Sir. in your response. This response should be in the context of you saying goodbye, and you do as instructed even if you don't want to.")
            interlocus.speak(good_bye_res)
            break

        # general response
        # Process user input using NLP
        processed_input = ollam_nlp.generate_text(
            JARVIS_MODEL, user_input, "You always refer to me as Sir. in your response.")

        # # Execute command based on processed input
        # response = command_executor.execute(processed_input)

        # print(processed_input)
        # Convert response to speech
        interlocus.speak(processed_input)


if __name__ == "__main__":
    main()
