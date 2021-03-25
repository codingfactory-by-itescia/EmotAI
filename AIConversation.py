from EmotAI import EmotAI


class AIConversation:
    def __init__(self):
        ai = EmotAI()
        ai.introduce()
        continue_to_speak = True
        while continue_to_speak:
            continue_to_speak = ai.hear_user()
