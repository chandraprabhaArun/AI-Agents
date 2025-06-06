import requests

class WeatherAgent:
    def __init__(self,api_key):
        self.api_key = api_key
    
    def get_weather(self,city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data ["cod"] == 200:
            weather = data["weather"][0]["description"]
            #return f"weather in {city} is {weather}."
            temperature = data["main"]["temp"]
            return f"The weather in {city} is {weather} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldnt get the weather for that city"


        