import ollama
import asyncio

# from tools.sky_color import SkyColor
# from tools.greet_user import GreetUser
# from tools.current_weather import CurrentWeather
# from tools.duckduckgo_search import DuckDuckGoSearch

from modules.tools.sky_color import SkyColor
from modules.tools.greet_user import GreetUser
from modules.tools.get_current_weather import CurrentWeather
from modules.tools.duckduckgo_search import DuckDuckGoSearch
from modules.tools.google_search import SearchTool
from modules.tools.current_time_tool import CurrentTimeTool
from modules.tools.current_date_tool import CurrentDateTool
from modules.tools.youtube_tool import YouTubeTool
from modules.tools.battery_level_tool import BatteryLevelTool
from modules.tools.iot.bulbs.tapo.tapo_l530 import DeviceTapoL530

class OllamaNLP:

    def __init__(self):
        # Instantiate tool classes
        self.sky_color = SkyColor()
        self.greet_user = GreetUser()
        self.current_weather = CurrentWeather()
        self.duckduckgo_search = DuckDuckGoSearch()
        self.search_tool = SearchTool() # google search tool
        self.current_time_tool = CurrentTimeTool() # current time tool
        self.current_date_tool = CurrentDateTool() # current date tool
        self.youtube_tool = YouTubeTool() # youtube tool
        self.battery_level_tool = BatteryLevelTool() # battery level tool
        self.tapo_l530 = DeviceTapoL530() # tapo l530 smart bulb
        
        # Initialize the message history list
        self.messages = []


    def generate_text(self, model, prompt, systemPrompt=""):

        user_message = prompt  # setting prompt to user_message
        function_result = None

        # Add system prompt once if not already added
        if not self.messages:
            if systemPrompt:
                self.messages.append({'role': 'system', 'content': systemPrompt})
            else:
                self.messages.append({
                    'role': 'system',
                    'content': 'You are Jarvis, a helpful AI assistant from the Iron Man movie. You only respond with short answers and refer to me as "Sir".'
                })

        # Check each tool's trigger phrases to determine if a specific function needs to be called
        if any(phrase in prompt.lower() for phrase in self.sky_color.trigger_phrases()):
            function_result = self.sky_color.get_info()
        elif any(phrase in prompt.lower() for phrase in self.greet_user.trigger_phrases()):
            function_result = self.greet_user.greet()
        elif any(phrase in prompt.lower() for phrase in self.current_weather.trigger_phrases()):
            # Extract city name for the weather function
            city = prompt.split("in")[-1].strip()
            function_result = self.current_weather.get_current_weather(city)
        elif any(phrase in prompt.lower() for phrase in self.duckduckgo_search.trigger_phrases()):
            # Extract search query for DuckDuckGo
            query = prompt
            for phrase in self.duckduckgo_search.trigger_phrases():
                query = query.replace(phrase, "")
            function_result = self.duckduckgo_search.duckduckgo_search(query.strip())
        elif any(phrase in prompt.lower() for phrase in self.search_tool.trigger_phrases()):
            # Perform a Google search
            function_result = self.search_tool.perform_search(prompt)
        elif any(phrase in prompt.lower() for phrase in self.current_time_tool.trigger_phrases()):
            function_result = self.current_time_tool.get_current_time()
        elif any(phrase in prompt.lower() for phrase in self.current_date_tool.trigger_phrases()):
            function_result = self.current_date_tool.get_current_date()
        elif any(phrase in prompt.lower() for phrase in self.youtube_tool.trigger_phrases()):
            # Play a video on YouTube
            function_result = self.youtube_tool.play_video(prompt)
        elif any(phrase in prompt.lower() for phrase in self.battery_level_tool.trigger_phrases()):
            function_result = self.battery_level_tool.get_battery_level()
        elif any(phrase in prompt.lower() for phrase in self.tapo_l530.trigger_phrases()):
            # Control the Tapo L530 smart bulb
            if "turn on" in prompt.lower():
                function_result = asyncio.run(self.tapo_l530.turn_on())
            elif "turn off" in prompt.lower():
                function_result = asyncio.run(self.tapo_l530.turn_off())
            elif "set brightness" in prompt.lower() or "set bulb to" in prompt.lower() or "adjust light" in prompt.lower() or "set the brightness" in prompt.lower():
                # Extract the brightness level from the prompt.lower()
                brightness_level = int(prompt.lower().split("to")[-1].replace("%", "").strip())
                function_result = asyncio.run(self.tapo_l530.set_brightness(brightness_level))
            elif "set color" in prompt.lower() or "change color" in prompt.lower() or "set the color" in prompt.lower() or "change light color" in prompt.lower() or "set the color" in prompt.lower():
                # Extract the color name from the prompt.lower()
                color_name = prompt.lower().split("to")[-1].strip()
                function_result = asyncio.run(self.tapo_l530.set_color(color_name))
            elif "set color temperature" in prompt.lower() or "set color temperature" in prompt.lower():
                # Extract the temperature value from the prompt.lower() (e.g., "set color temperature to 2700")
                color_temp = int(prompt.lower().split("to")[-1].strip())
                function_result = asyncio.run(self.tapo_l530.set_color_temperature(color_temp))
            elif "set hue" in prompt.lower() or "set saturation" in prompt.lower() or "set the saturation" in prompt.lower():
                # Extract hue and saturation values from the prompt.lower() (e.g., "set hue to 195 and saturation to 100")
                parts = prompt.lower().split("and")
                hue = int(parts[0].split("to")[-1].strip())
                saturation = int(parts[1].split("to")[-1].strip())
                function_result = asyncio.run(self.tapo_l530.set_hue_saturation(hue, saturation))
            elif "status" in prompt.lower() or "bulb status" in prompt.lower() or "smart bulb status" in prompt.lower():
                # Get the current status of the bulb
                function_result = asyncio.run(self.tapo_l530.status())
            else:
                function_result = "I'm sorry, I couldn't understand that command. Please try again."

        # Construct the system prompt if a tool function was triggered
        if function_result:
            print("---------------------------------")
            print(f"Function call: {function_result}")
            print("---------------------------------")
            systemPrompt = (
                f"You are restricted to this information in your response: {function_result}. "
                "Use it as context to respond accurately. Always stay within the scope of this data and do not be creative."
            )


        if systemPrompt:
            # Add system prompt as a message with role 'system' if available
            self.messages.append({'role': 'system', 'content': systemPrompt})
        else:
            # Add an custom system prompt
            self.messages.append({'role': 'system', 'content': 'You are Jarvis, a helpful AI assistant from the iron man movie and you only respond with short answers, you refer to me as Sir.'})


        # Add the current user prompt to the message history
        self.messages.append({'role': 'user', 'content': user_message})

        # We now call ollama.chat
        try:
            # print("working---------------------------------")
            # print(f"Messages: {messages}")
            # print("working---------------------------------")
            response = ollama.chat(model=model, messages=self.messages)
            assistant_reply = response['message']['content']

            # Append the assistant's reply to the message history
            self.messages.append({'role': 'assistant', 'content': assistant_reply})

            # Extract and return the content from the response
            return assistant_reply
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            self.messages.append({'role': 'assistant', 'content': error_message})
            return error_message

# Test the OllamaNLP class
# if __name__ == "__main__":
#     nlp = OllamaNLP()
#     model = "fotiecodes/jarvis:3b"
#     prompt = "What is the weather like in Bamenda"
#     system_prompt = ""
    
#     result = nlp.generate_text(model, prompt, systemPrompt=system_prompt)
#     print(result)









# import requests
# import json


# class OllamaNLP:

#     def __init__(self, base_url='http://localhost:11434'):
#         self.base_url = base_url

#     def generate_text(self, model, prompt, systemPrompt="", stream=False, options=None):
#         endpoint = f'{self.base_url}/api/generate'

#         # prompt = "<s>[INST] <<SYS>>You are Jarvis, a helpful AI assistant from the iron man movie and you only respond with short answers, you refer to me as Sir. <</SYS>>"+prompt+"</s>",
#         prompt = f"<s>[INST] <<SYS>> { systemPrompt } <</SYS>> { prompt } [/INST] </s>"
#         payload = {
#             "model": model,
#             "prompt": prompt,
#             "options": options,
#             "stream": stream,
#         }

#         headers = {'Content-Type': 'application/json'}

#         response = requests.post(
#             endpoint, data=json.dumps(payload), headers=headers)

#         if response.status_code == 200:
#             response_json = json.loads(response.text)
#             if 'response' in response_json:
#                 return response_json['response']
#             else:
#                 return {"error": "Response field not found in the API response."}
#         else:
#             return {"error": f"Error {response.status_code}: {response.text}"}
