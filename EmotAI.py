from MemoryData import MemoryData
from ReactionStrategies.LaughStrategy import LaughStrategy
from ReactionStrategies.SmileStrategy import SmileStrategy
from ReactionStrategies.AgressiveStrategy import AgressiveStrategy
from ReactionStrategies.CryStrategy import CryStrategy
from ReactionStrategies.DefaultStrategy import DefaultStrategy


class EmotAI:
    NAME_OF_MEMORY_INDEX = 0
    VALUE_OF_MEMORY_INDEX = 1
    MEMORY_SIZE = 10

    def __init__(self, personality):
        self.personality = personality
        self.knowledge = self.take_knowledge()
        self.actions_memory = MemoryData(personality["memory"], self.MEMORY_SIZE)

        self.personalities_strategies = [
            LaughStrategy(self),
            SmileStrategy(self),
            AgressiveStrategy(self),
            CryStrategy(self),
            DefaultStrategy(self)
        ]

    def take_knowledge(self):
        f = open("memoryOfEmotAI.txt", "r")
        my_dict = {}
        for memoryLine in f:
            splitted_memories = memoryLine.replace("\n", "").split('=')
            my_dict[splitted_memories[self.NAME_OF_MEMORY_INDEX]] = splitted_memories[self.VALUE_OF_MEMORY_INDEX]
        return my_dict

    def say(self, sentence):
        print(sentence)

    def introduce(self):
        self.say("Hello I am " + str(self.knowledge.get("myName")) + " ! I was born on the " + str(
            self.knowledge.get("myBirthDate")))

    # return True to continue
    # return False to stop
    def hear_user(self):
        to_analyze = input("Please send me a word : ")
        if str.lower(to_analyze.strip()) == "stop" or str.lower(to_analyze.strip()) == "bye":
            self.say("Ok, bye !")
            return False
        elif str.lower(to_analyze) == "hit":
            self.hit()
            return True
        elif str.lower(to_analyze) == "joke":
            self.joke()
            return True
        else:
            self.say("You said \"" + to_analyze + "\" but I did not understand. If you want to stop, just tell me STOP")
            return True

    def how_do_you_feel(self):
        self.say("For the moment...")

    def hit(self):
        for personality in self.personalities_strategies:
            if personality.is_personality["hit"]:
                return personality.hit()

    def joke(self):
        for personality in self.personalities_strategies:
            if personality.is_personality["joke"]:
                return personality.joke()
