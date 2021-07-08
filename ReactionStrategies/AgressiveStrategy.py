from utils import handle_reaction

class AgressiveStrategy:
    hit_table = [
        "Don't you have anything better to do ?",
        "Stop it now !",
        "I want to hit you !",
        "Son of a glitch !",
        "Okay, i'm going out to piss you off !"
    ]
    joke_table = [
        "Hahahahaha",
        "Hohahaha",
        "Whahahaha",
        "NYAHAHAHA",
    ]
    look_table = [
        "What do you look ?",
        "What are you doig !",
        "Get lost !"
    ]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": emot_ai.personality["sensible"] and emot_ai.personality["impulsive"] and emot_ai.personality["pessimistic"] and emot_ai.personality["demonstrative"],
            "joke": emot_ai.personality["impulsive"] and emot_ai.personality["demonstrative"] and emot_ai.personality["extrovert"],
            "look": emot_ai.personality["impulsive"]
        }

    def hit(self):
        handle_reaction(self.emot_ai, self.hit_table, "hit")
        should_continue = not self.emot_ai.actions_memory.count_value("hit") > len(self.hit_table)
        return should_continue

    def joke(self):
        handle_reaction(self.emot_ai, self.joke_table, "joke")
        return True

    def look(self):
        handle_reaction(self.emot_ai, self.look_table, "look")
        return True