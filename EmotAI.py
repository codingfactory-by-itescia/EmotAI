from MemoryData import MemoryData

class EmotAI:
    NAME_OF_MEMORY_INDEX = 0
    VALUE_OF_MEMORY_INDEX = 1
    MEMORY_SIZE = 10
    hit_table_laugh = ["^^","^^’","Haha !", "xD"]

    def __init__(self, personality):
        self.personality = personality
        self.knowledge = self.take_knowledge()
        self.actions_memory = MemoryData(personality["memory"],self.MEMORY_SIZE)

    def take_knowledge(self):
        f = open("memoryOfEmotAI.txt", "r")
        my_dict = {}
        for memoryLine in f:
            splitted_memories = memoryLine.replace("\n","").split('=')
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
        else:
            self.say("You said \"" + to_analyze + "\" but I did not understand. If you want to stop, just tell me STOP")
            return True

    def how_do_you_feel(self):
        self.say("For the moment...")

    def hit(self):
        #laugh
        if self.personality["extrovert"] and self.personality["impulsive"] and not self.personality["pessimistic"] and self.personality["demonstrative"]:
            self.say(self.react(self.hit_table_laugh,self.actions_memory.count_value("hit")))
        if not self.personality["extrovert"] and not self.personality["pessimistic"] and not self.personality["impulsive"]:
            pass
        if self.personality["sensible"] and self.personality["impulsive"] and self.personality["pessimistic"] and self.personality["demonstrative"]:
            pass
        if self.personality["sensible"] and self.personality["pessimistic"] and self.personality["demonstrative"]:
            pass
        self.actions_memory.add("hit")

    def react(self,responses, count):
        if count >= len(responses):
            return responses[len(responses)-1]
        return responses[count]


