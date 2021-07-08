from utils import handle_reaction

class CryStrategy:
    hit_table = [
        "Outch",
        "Why did you do that ?",
        "I want to hit you !",
        "Here is my money.",
        "Good bye Cruel World !"
    ]
    joke_table = [
        "Sorry but I am not ready to laugh !",
        "…",
        ":|",
        ":’]",
        ":]"
    ]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": emot_ai.personality["sensible"] and emot_ai.personality["pessimistic"] and emot_ai.personality["demonstrative"],
            "joke": emot_ai.personality["pessimistic"] and emot_ai.personality["impulsive"]
        }

    def hit(self):
        handle_reaction(self.emot_ai, self.hit_table, "hit")
        should_continue = not self.emot_ai.actions_memory.count_value("hit") > len(self.hit_table)
        return should_continue

    def joke(self):
        handle_reaction(self.emot_ai, self.joke_table, "joke")
        return True