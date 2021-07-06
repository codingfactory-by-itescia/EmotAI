from utils import react

class AgressiveStrategy:
    hit_table = [
        "Don't you have anything better to do ?",
        "Stop it now !",
        "I want to hit you !",
        "Son of a glitch !",
        "Okay, i'm going out to piss you off !"
    ]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality_on_hit = {
            "hit": emot_ai.personality["sensible"] and emot_ai.personality["impulsive"] and emot_ai.personality["pessimistic"] and emot_ai.personality["demonstrative"],
            "joke": emot_ai.personality["impulsive"] and emot_ai.personality["demonstrative"] and emot_ai.personality["extrovert"]
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
