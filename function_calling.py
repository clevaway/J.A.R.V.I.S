# this is a simple attempt at addting function calling to ollama

import ollama
import requests

# Define functions directly without a registry
def sky_color():
    return "The sky appears blue due to Rayleigh scattering, where shorter blue wavelengths scatter more in all directions."

def greet_user(name="Fotie"):
    return f"Hello, {name}! How can I assist you today?"
def current_weather(city):
    try:
        # Geocoding API to find latitude and longitude for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        # Check if the city was found and get coordinates
        if "results" in geo_data and len(geo_data["results"]) > 0:
            latitude = geo_data["results"][0]["latitude"]
            longitude = geo_data["results"][0]["longitude"]
            url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
            
            # Get the weather data
            weather_response = requests.get(url)
            weather_data = weather_response.json()
            current_weather = weather_data.get("current_weather", {})
            
            if current_weather:
                # Gather available weather data
                temp = current_weather.get("temperature", "N/A")
                wind_speed = current_weather.get("windspeed", "N/A")
                wind_direction = current_weather.get("winddirection", "N/A")
                
                # Check for and interpret weather condition code
                condition = current_weather.get("weathercode", "N/A")
                conditions_map = {
                    0: "clear sky",
                    1: "mainly clear",
                    2: "partly cloudy",
                    3: "overcast",
                    45: "fog",
                    48: "depositing rime fog",
                    51: "light drizzle",
                    53: "moderate drizzle",
                    55: "dense drizzle",
                    56: "light freezing drizzle",
                    57: "dense freezing drizzle",
                    61: "slight rain",
                    63: "moderate rain",
                    65: "heavy rain",
                    66: "light freezing rain",
                    67: "heavy freezing rain",
                    71: "slight snowfall",
                    73: "moderate snowfall",
                    75: "heavy snowfall",
                    77: "snow grains",
                    80: "slight rain showers",
                    81: "moderate rain showers",
                    82: "violent rain showers",
                    85: "slight snow showers",
                    86: "heavy snow showers",
                    95: "thunderstorm",
                    96: "thunderstorm with slight hail",
                    99: "thunderstorm with heavy hail"
                }
                weather_condition = conditions_map.get(condition, "unknown condition")

                # Build response with available fields only
                response_parts = [
                    f"Temperature in {city} is {temp}°C with {weather_condition}.",
                    f"Wind speed is {wind_speed} km/h" if wind_speed != "N/A" else "",
                    f"Wind direction is {wind_direction}°" if wind_direction != "N/A" else ""
                ]
                # Filter out any empty strings and join parts into a single response
                return " ".join(part for part in response_parts if part)
                
            else:
                return f"Sorry, I couldn't retrieve the current weather for {city}."
        else:
            return f"City '{city}' not found."

    except Exception as e:
        return f"An error occurred while retrieving the weather data: {e}"
# Enhanced Ollama chat function with function results passed back to LLM
def ollama_chat_with_function_call(model, user_message):
    # Determine the function to call based on keywords in the user's message
    function_result = None
    if "sky" in user_message.lower() and "color" in user_message.lower():
        function_result = sky_color()
    elif "greet" in user_message.lower() or "hello" in user_message.lower():
        function_result = greet_user()
    elif "weather" in user_message.lower():
        city = user_message.split("in")[-1].strip()  # Extract city from message
        function_result = current_weather(city)

    if function_result:
        print(f"Function result: {function_result}")
        print("---------------------------------")
        # Pass function result back to LLM for final response
        response = ollama.chat(model=model, messages=[
            {'role': 'system', 'content': f"You are grounded to this response from the api: {function_result}. Use it as context to respond accurately. always stay within the scope of this data and do note be creative."},
            {'role': 'user', 'content': user_message}
        ])
        return response

    # Default to standard Ollama chat if no function is called
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': user_message}])
    return response

# Testing the functionality
if __name__ == "__main__":
    # Example questions
    response = ollama_chat_with_function_call('jarvis:3b', 'Why is the sky blue?')
    print(response['message']['content'])
    print("##########################################")

    response = ollama_chat_with_function_call('jarvis:3b', 'Can you greet me?')
    print(response['message']['content'])
    print("##########################################")

    response = ollama_chat_with_function_call('jarvis:3b', 'What is the weather like in Bamenda')
    print(response['message']['content'])