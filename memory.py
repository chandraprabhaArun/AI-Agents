class MemoryAgent:
    def __init__(self):
        self.rules = {
            "hello" : "Hi, there",
            "hi hello" : "how r u",
            "bye" : "Good Bye",
            "default" : "Im Sorry, I dont understand",
        }
        self.memory = []

    def respond(self, user_input):
        self.memory.append(f"You: {user_input}")
        user_input = user_input.lower().strip()

        if user_input.startswith["my name is "]:
            name = user_input[11:]
            self.memory.append(f"Agent : Got it, Your name is {name}!")
            return f"Got it Your name is, {name}!"
        elif user_input == "whats your name?" and any("Your name is" in m for m in self.memory):
            for m in reversed(self.memory):
                if "Your name is" in m:
                    name = m.split ("Your name is" )[1].strip("!")
                    return f" I remember, your name is {name}!"
        return self.rules.get(user_input, "I dont get it")       




