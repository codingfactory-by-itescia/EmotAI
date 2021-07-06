from utils import react

class CryStrategy:
    hit_table = [
        "Outch",
        "Why did you do that ?",
        "I want to hit you !",
        "Here is my money.",
        "Good bye Cruel World !"
    ]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": emot_ai.personality["sensible"] and emot_ai.personality["pessimistic"] and emot_ai.personality["demonstrative"],
            "joke": True
        }

    def hit(self):
        self.emot_ai.say(
            react(
                self.hit_table,
                self.emot_ai.actions_memory.count_value("hit")
            )
        )
        self.emot_ai.actions_memory.add("hit")

        should_continue = not self.emot_ai.actions_memory.count_value("hit") > len(self.hit_table)
        return should_continue

    def joke(self):
        pass