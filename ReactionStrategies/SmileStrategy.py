from utils import react

class SmileStrategy:
    hit_table = [":o", ":|", ":)", ":>", ":D"]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": not emot_ai.personality["extrovert"] and not emot_ai.personality["pessimistic"] and not emot_ai.personality["impulsive"],
            "joke": emot_ai.personality["sensible"] and not emot_ai.personality["extrovert"]
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

