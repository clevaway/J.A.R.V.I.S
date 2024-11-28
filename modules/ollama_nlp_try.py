import ollama

# # when we calling for prod
# from modules.tools.get_current_weather import CurrentWeather

# when we calling  for test
from tools.get_current_weather import CurrentWeather

import requests
import json


class OllamaNLP:

    def __init__(self, base_url='http://localhost:11434'):
        self.base_url = base_url
        # Map tool names to their corresponding functions
        self.tool_map = {
            "get_current_weather": CurrentWeather.get_current_weather,
        }

    def generate_text(self, model, prompt, stream=False, options=None):
        endpoint = f'{self.base_url}/api/generate'

        # prompt = "<s>[INST] <<SYS>>You are Jarvis, a helpful AI assistant from the iron man movie and you only respond with short answers, you refer to me as Sir. <</SYS>>"+prompt+"</s>",
        systemPrompt ="""
            You are a helpful assistant with access to the following functions. Use them if required
        """
        prompt = f"""
        <|im_start|>system { systemPrompt }<|im_end|>
        <|im_start|>user{ prompt }<|im_end|>"""
        # prompt = f"<s>[INST] <<SYS>> { systemPrompt } <</SYS>> { systemPrompt } [/INST] </s>"
        payload = {
            "model": model,
            "prompt": prompt,
            "options": options,
            "stream": stream,
        }

        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            endpoint, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response_json = json.loads(response.text)
            if 'response' in response_json:
                return response_json['response']
            else:
                return {"error": "Response field not found in the API response."}
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}


# Test the OllamaNLP class
if __name__ == "__main__":
    nlp = OllamaNLP()
    model = "jarvis:3b"
    prompt = "What is the weather like in Ankara"
    
    result = nlp.generate_text(model, prompt, stream=False)
    print(result)



# class OllamaNLP:

#     def __init__(self):
#          # Map tool names to their corresponding functions
#         self.tool_map = {
#             "get_current_weather": CurrentWeather.get_current_weather,
#         }

#     def execute_tool(self, tool_name, parameters):
#         """
#         Dynamically executes a tool based on its name and parameters.
#         """
#         if tool_name in self.tool_map:
#             tool_function = self.tool_map[tool_name]
#             try:
#                 # Call the function with parameters if applicable
#                 if parameters:
#                     return tool_function(**parameters)
#                 else:
#                     return tool_function()
#             except Exception as e:
#                 return f"Error executing {tool_name}: {e}"
#         else:
#             return f"Tool {tool_name} not found."

#     def generate_text(self, model, prompt, systemPrompt="", stream=False, options=None):
#         messages = [{'role': 'system', 'content': "You are a helpful assistant with access to the following functions. Use them if required"+systemPrompt}] if systemPrompt else []
#         messages.append({'role': 'user', 'content': prompt})
        
#         tools = [{
#             'type': 'function',
#             'function': {
#                 'name': 'get_current_weather',
#                 'description': 'Get the current weather for a city',
#                 'parameters': {
#                     'type': 'object',
#                     'properties': {
#                         'city': {
#                             'type': 'string',
#                             'description': 'The name of the city',
#                         },
#                     },
#                     'required': ['city'],
#                 },
#             },
#         }]
        
#         try:
#             response = ollama.chat(
#                 model=model,
#                 messages=messages,
#                 stream=stream,
#                 tools=tools,
#                 **(options or {})
#             )
#             print(response)
            
#             # Handle the tool calling
#             if response.get("tool_name"):
#                 tool_name = response["tool_name"]
#                 parameters = response.get("parameters", {})
                
#                 # Execute the tool
#                 tool_result = self.execute_tool(tool_name, parameters)
                
#                 # Check for tool output and include it in the final response
#                 if tool_result:
#                     return {"tool_output": tool_result}
#                 else:
#                     return {"error": f"Tool {tool_name} did not return any output."}
            
#             # Return the assistant's regular response if no tool is called
#             return response.get("text", "No response generated.")

#         except Exception as e:
#             return {"error": str(e)}

