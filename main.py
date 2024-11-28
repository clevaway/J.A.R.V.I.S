from modules.vibranium.vision.vision import Vision
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
    # text_to_speech = TextToSpeech()
    interlocus = Interlocus()
    
    ollam_nlp = OllamaNLP()

    # init vibranium modules
    vision = Vision()
    # command_executor = CommandExecutor()

    # Load configuration
    # config = Config()
    # run intro
    # run_introduction()

    while True:
        # Listen for user input
        user_input = interlocus.listen()


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
                JARVIS_MODEL, user_input, "You have been asked to shutdown, say goodbye to the user.")
            interlocus.speak(good_bye_res)
            break

        # general response
        # Process user input using NLP
        processed_input = ollam_nlp.generate_text(
            JARVIS_MODEL, user_input)

        # # Execute command based on processed input
        # response = command_executor.execute(processed_input)

        # print(processed_input)
        # Convert response to speech
        interlocus.speak(processed_input)


if __name__ == "__main__":
    main()
