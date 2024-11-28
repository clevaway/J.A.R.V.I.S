# tools/current_weather.py

import requests

class CurrentWeather:
    @staticmethod
    def trigger_phrases():
        return ["weather", "what's the weather", "current weather in", "weather forecast"]

    @staticmethod
    def get_current_weather(city):
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
                    temp = current_weather.get("temperature", "N/A")
                    # Interpret weather condition
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
                    return f"The temperature in {city} is {temp}°C, with {weather_condition}."
                else:
                    return f"Sorry, I couldn't retrieve the current weather for {city}."
            else:
                return f"Having troubles finding this city."

        except Exception as e:
            return f"An error occurred while retrieving the weather data: {e}"