from utils import react_with_random

class LaughStrategy:
    hit_table = ["^^", "^^’", "Haha !", "xD"]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": emot_ai.personality["extrovert"] and emot_ai.personality["impulsive"] and not emot_ai.personality["pessimistic"] and emot_ai.personality["demonstrative"],
            "joke": True
        }

    def hit(self):
        self.emot_ai.say(
            react_with_random(
                self.hit_table,
                self.emot_ai.actions_memory.count_value("hit")
            )
        )
        self.emot_ai.actions_memory.add("hit")
        return True

    def joke(self):
        pass
