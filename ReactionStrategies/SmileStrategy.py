from utils import handle_reaction,handle_with_random_reaction

class SmileStrategy:
    hit_table = [":o", ":|", ":)", ":>", ":D"]
    joke_table = ["...","Hhh...", "Hihihi", "Ha…ha", "Hahaha !" ]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": not emot_ai.personality["extrovert"] and not emot_ai.personality["pessimistic"] and not emot_ai.personality["impulsive"],
            "joke": emot_ai.personality["sensible"] and not emot_ai.personality["extrovert"]
        }

    def hit(self):
        handle_reaction(self.emot_ai, self.hit_table, "hit")
        return True

    def joke(self):
        handle_with_random_reaction(self.emot_ai, self.joke_table, "joke")
        return True

