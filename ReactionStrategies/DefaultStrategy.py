from utils import react

class DefaultStrategy:
    hit_table = [
        "Huh ?",
        "Did something happen ?",
        "I don’t understand.",
        "Hm.",
        "..."
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
        return True

    def joke(self):
        pass