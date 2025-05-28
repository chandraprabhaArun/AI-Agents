from .weather import WeatherAgent

class ChatAgent:
    def __init__(self,weather__api__key):
      self.memory = []
      self.weather_agent = WeatherAgent(weather__api__key)

    def respond(self, user_input):
       self.memory.append(f"you: {user_input}")
       user_input = user_input.lower().strip()

       if user_input.startswith(" weather in "):
          city = user_input[11:]
          weather = self.weather_agent.get_weather(city)
          return f"Its {weather} in {city}." if weather else "I don't know. Couldnt find weather"
        
       return "Ask me about the weather or something else"
        



    
    