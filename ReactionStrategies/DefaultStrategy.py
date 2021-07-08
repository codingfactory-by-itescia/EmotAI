from utils import handle_reaction

class DefaultStrategy:
    hit_table = [
        "Huh ?",
        "Did something happen ?",
        "I don’t understand.",
        "Hm.",
        "..."
    ]
    joke_table = [
        "...",
        "That is supposed to be fun ?",
        "Have you finished joking ?",
        "Leave me alone."]
    look_table = [
        "Do I have something in my teeth ?",
        ":-|",
        "Stop that !"
    ]

    def __init__(self, emot_ai):
        self.emot_ai = emot_ai
        self.is_personality = {
            "hit": True,
            "joke": True,
            "look": True
        }



    def hit(self):
        handle_reaction(self.emot_ai, self.hit_table, "hit")
        return True

    def joke(self):
        handle_reaction(self.emot_ai, self.joke_table, "joke")
        return True

    def look(self):
        handle_reaction(self.emot_ai, self.look_table, "look")
        return True
