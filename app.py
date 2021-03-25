from AIConversation import AIConversation
from EmotAI import EmotAI
from PersonalityParser import PersonalityParser

loadedPersonality = PersonalityParser.parse("personality1")

loadedPersonality['sensible'] = True

PersonalityParser.save("personality1", loadedPersonality)

# c = AIConversation()

