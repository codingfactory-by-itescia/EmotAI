from AIConversation import AIConversation
from EmotAI import EmotAI
from PersonalityParser import PersonalityParser

loadedPersonality = PersonalityParser.parse("personality2")

# loadedPersonality['sensible'] = True

# PersonalityParser.save("personality2", loadedPersonality)

c = AIConversation(loadedPersonality)

