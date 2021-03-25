class EmotAI:
    NAME_OF_MEMORY_INDEX = 0
    VALUE_OF_MEMORY_INDEX = 1
    def __init__(self):

        self.myMemory=self.take_memory()

    def take_memory(self):
        f = open("memoryOfEmotAI.txt", "r")
        my_dict = {}
        for memoryLine in f:
            splitted_memories = memoryLine.split('=')
            my_dict[splitted_memories[self.NAME_OF_MEMORY_INDEX]] = splitted_memories[self.VALUE_OF_MEMORY_INDEX]
        return my_dict
    def say(self, sentence):
        print(sentence)

    def introduce(self):
        self.say("Hello I am " + str(self.myMemory.get("myName"))+" ! I was born on the " + str(self.myMemory.get("myBirthDate")))

    #return True to continue
    #return False to stop
    def hear_user(self):
        to_analyze = input("Please send me a word : ")
        if str.lower(to_analyze) == "stop":
            self.say("Ok, bye !")
            return False
        elif str.lower(to_analyze) == "hit":
            self.hit()
        else:
            self.say("You said \""+to_analyze+"\" but I did not understand. If you want to stop, just tell me STOP")
            return True

    def how_do_you_feel(self):
        self.say("For the moment...")

    def hit(self):
        if self.personality["sensible"]:
            self.say("AÎE !")
