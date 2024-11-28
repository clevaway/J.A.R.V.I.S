# tools/current_date_tool.py

from datetime import datetime

class CurrentDateTool:
    @staticmethod
    def trigger_phrases():
        """
        Return a list of phrases that trigger the current date tool.
        """
        return ["what's the date", "current date", "today's date", "tell me the date", "date today"]

    @staticmethod
    def get_current_date():
        """
        Get the current date in a human-readable format: Day of the week, Month day, Year.
        """
        current_date = datetime.now()
        res = current_date.strftime("%A, %B %d, %Y")  # Format: Day of the week, Month day, Year
        # print("Current date:", res)
        return res
