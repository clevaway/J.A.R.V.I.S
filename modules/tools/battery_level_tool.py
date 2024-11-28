# tools/battery_level_tool.py

import psutil

class BatteryLevelTool:
    @staticmethod
    def trigger_phrases():
        """
        Return a list of phrases that trigger the battery level tool.
        """
        return ["battery level", "current battery", "battery status", "how much battery", "check battery"]

    @staticmethod
    def get_battery_level():
        """
        Get the current battery level as a percentage and charging status.
        """
        battery = psutil.sensors_battery()
        if battery is not None:
            percentage = battery.percent
            charging = battery.power_plugged
            status = "charging" if charging else "not charging"
            response = f"The battery level is {percentage}% and it is currently {status}."
        else:
            response = "Battery information is not available on this device."
        
        print("Battery level:", response)  # Optional: for debugging
        return f"Battery level and status: {response}"
