from EmotAI import EmotAI
class AIConversation:
    def __init__(self):
        ai = EmotAI()
        ai.introduce()
        continueToSpeak = True
        while continueToSpeak:
            continueToSpeak=ai.hearUser()


