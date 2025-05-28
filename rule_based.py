class RuleBasedAgent:
    def __init__(self):
        self.rules = {
            "hello" : "Hi, there",
            "hi hello" : "how r u",
            "bye" : "Good Bye",
            "default" : "Im Sorry, I dont understand"
        }

    def respond(self, user_input):
        user_input = user_input.lower().strip()
        return self.rules.get(user_input, self.rules["default"])
