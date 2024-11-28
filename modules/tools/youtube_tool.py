# tools/youtube_tool.py

import webbrowser
import pywhatkit as kit

class YouTubeTool:
    @staticmethod
    def trigger_phrases():
        """
        Return a list of phrases that trigger the YouTube tool.
        """
        return ["play", "play on youtube", "watch", "find on youtube"]

    @staticmethod
    def play_video(user_input):
        """
        Open YouTube and search for the specified video based on user input.
        """
        # Convert user_input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()

        # Check if any trigger phrase is in the input
        trigger_phrase = next((phrase for phrase in YouTubeTool.trigger_phrases() if phrase in user_input_lower), None)

        if trigger_phrase:
            # Split the input to get the video title after the trigger phrase
            parts_after_trigger = user_input_lower.split(trigger_phrase, 1)

            if len(parts_after_trigger) > 1:
                # Extract the video title after the trigger phrase
                video = ' '.join(parts_after_trigger[1].split())

                # Construct the YouTube search URL
                kit.playonyt(video)

                # Provide spoken feedback or print confirmation
                return f"Playing on YouTube."