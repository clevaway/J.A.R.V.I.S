# tools/iot/bulbs/tapo/tapo_l530.py

import os
from tapo import ApiClient
from tapo.requests import Color
from dotenv import load_dotenv

load_dotenv(override=True)

# loading env variables
TAPO_USERNAME = os.getenv('TAPO_USERNAME')
TAPO_PASSWORD = os.getenv('TAPO_PASSWORD')


class DeviceTapoL530:
    
    def __init__(self):
        """
        Initialize the DeviceTapoL530 with login credentials and IP address.
        """
        self.tapo_username = TAPO_USERNAME
        self.tapo_password = TAPO_PASSWORD
        self.ip_address = "192.168.1.35"  # IP address of the smart bulb "192.168.1.34", "192.168.1.33", "192.168.1.35"

        # Initialize the ApiClient
        self.client = ApiClient(self.tapo_username, self.tapo_password)
        
    async def _connect_device(self):
        """
        Connect to the smart bulb device using the provided IP address.
        """
        device = await self.client.l530(self.ip_address)  # Assuming L530 model is used
        print(f"Connected to device: {device}")
        return device

    def trigger_phrases(self):
        """
        Return a list of trigger phrases to activate the smart bulb control tool.
        """
        return [
            "turn on the light", "turn off the light", "set brightness", "set the brightness", "set color", "set the color", "change color", 
            "set bulb to", "control bulb", "adjust light", "adjust brightness", "change brightness", "change light color", "set color temperature", 
            "bulb status", "smart bulb status", "smart bulb info", "set saturation", "set the saturation"
        ]

    async def turn_on(self):
        """
        Turn the smart bulb on.
        """
        device = await self._connect_device()
        await device.on()
        return "The light has been turned on."

    async def turn_off(self):
        """
        Turn the smart bulb off.
        """
        print("💡 Turning off lights")
        device = await self._connect_device()
        await device.off()
        return "The light has been turned off."

    async def set_brightness(self, brightness_level):
        """
        Set the brightness of the smart bulb (0 to 100%).
        """
        if not 0 <= brightness_level <= 100:
            return "Brightness level must be between 0 and 100."

        device = await self._connect_device()
        await device.set_brightness(brightness_level)
        return f"The brightness has been set to {brightness_level}%."

    async def set_color(self, color_name):
        """
        Set the color of the smart bulb using a predefined color.
        """
        color_mapping = {
            "cool white": Color.CoolWhite,
            "daylight": Color.Daylight,
            "ivory": Color.Ivory,
            "warm white": Color.WarmWhite,
            "incandescent": Color.Incandescent,
            "candlelight": Color.Candlelight,
            "snow": Color.Snow,
            "ghost white": Color.GhostWhite,
            "alice blue": Color.AliceBlue,
            "light goldenrod": Color.LightGoldenrod,
            "lemon chiffon": Color.LemonChiffon,
            "antique white": Color.AntiqueWhite,
            "gold": Color.Gold,
            "peru": Color.Peru,
            "chocolate": Color.Chocolate,
            "sandy brown": Color.SandyBrown,
            "coral": Color.Coral,
            "pumpkin": Color.Pumpkin,
            "tomato": Color.Tomato,
            "vermillion": Color.Vermilion,
            "orange red": Color.OrangeRed,
            "pink": Color.Pink,
            "crimson": Color.Crimson,
            "dark red": Color.DarkRed,
            "hot pink": Color.HotPink,
            "smitten": Color.Smitten,
            "medium purple": Color.MediumPurple,
            "blue violet": Color.BlueViolet,
            "indigo": Color.Indigo,
            "light sky blue": Color.LightSkyBlue,
            "cornflower blue": Color.CornflowerBlue,
            "ultramarine": Color.Ultramarine,
            "deep sky blue": Color.DeepSkyBlue,
            "azure": Color.Azure,
            "navy blue": Color.NavyBlue,
            "light turquoise": Color.LightTurquoise,
            "aquamarine": Color.Aquamarine,
            "turquoise": Color.Turquoise,
            "light green": Color.LightGreen,
            "lime": Color.Lime,
            "forest green": Color.ForestGreen,
            "white": Color.CoolWhite,
        }

        if color_name.lower() not in color_mapping:
            return "Invalid color. Please choose a valid color."

        device = await self._connect_device()
        await device.set_color(color_mapping[color_name.lower()])
        return f"The color has been set to {color_name}."

    async def set_color_temperature(self, temperature):
        """
        Set the color temperature (Kelvin) of the bulb.
        """
        if not (2700 <= temperature <= 6500):
            return "Color temperature must be between 2700K and 6500K."

        device = await self._connect_device()
        await device.set_color_temperature(temperature)
        return f"The color temperature has been set to {temperature}K."

    async def set_hue_saturation(self, hue, saturation):
        """
        Set the color hue and saturation of the bulb.
        """
        if not (0 <= hue <= 360) or not (0 <= saturation <= 100):
            return "Hue must be between 0 and 360, and saturation must be between 0 and 100."

        device = await self._connect_device()
        await device.set_hue_saturation(hue, saturation)
        return f"The hue has been set to {hue} and saturation to {saturation}%."

    async def status(self):
            """
            Get the current status of the bulb.
            """
            device = await self._connect_device()
            device_info = await device.get_device_info()
            device_usage = await device.get_device_usage()

            return f"Device Info: {device_info.to_dict()}\nDevice Usage: {device_usage.to_dict()}"