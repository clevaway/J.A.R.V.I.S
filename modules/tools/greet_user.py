# tools/greet_user.py

class GreetUser:
    @staticmethod
    def greet(name="Fotie"):
        return f"Hello, {name}! How can I assist you today?"

    @staticmethod
    def trigger_phrases():
        return ["greet me", "hello", "say hi", "greet the user"]