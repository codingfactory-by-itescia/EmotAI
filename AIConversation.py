from EmotAI import EmotAI
from PersonalityParser import PersonalityParser


class AIConversation:
    def __init__(self, personality):
        ai = EmotAI(personality)
        ai.introduce()
        continue_to_speak = True
        while continue_to_speak:
            continue_to_speak = ai.hear_user()
