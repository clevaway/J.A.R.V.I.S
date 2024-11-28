# tools/current_time_tool.py

from datetime import datetime

class CurrentTimeTool:
    @staticmethod
    def trigger_phrases():
        """
        Return a list of phrases that trigger the current time tool.
        """
        return ["what time is it", "current time", "tell me the time", "time now", "what's the time"]

    @staticmethod
    def get_current_time():
        """
        Get the current time in a 12-hour clock format.
        """
        current_time = datetime.now()
        res = current_time.strftime("%I:%M %p")  # 12-hour clock format
        print("Current time:", res)
        return res
