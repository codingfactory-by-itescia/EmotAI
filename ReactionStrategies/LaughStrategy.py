from utils import handle_with_random_reaction

class LaughStrategy:
    hit_table = ["^^", "^^’", "Haha !", "xD"]
    joke_table = ["Hahahahaha"]


    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": emot_ai.personality["extrovert"] and emot_ai.personality["impulsive"] and not emot_ai.personality["pessimistic"] and emot_ai.personality["demonstrative"],
            "joke": emot_ai.personality["demonstrative"] and emot_ai.personality["extrovert"] and emot_ai.personality["impulsive"]
        }

    def hit(self):
        handle_with_random_reaction(self.emot_ai, self.hit_table, "hit")
        return True

    def joke(self):
        handle_with_random_reaction(self.emot_ai, self.joke_table, "joke")
        return True
