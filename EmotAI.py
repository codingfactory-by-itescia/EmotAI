class EmotAI:
    NAME_OF_MEMORY_INDEX = 0
    VALUE_OF_MEMORY_INDEX = 1
    def __init__(self):

        self.myMemory=self.takeMemory()

    def takeMemory(self):
        f = open("memoryOfEmotAI.txt", "r")
        myDict = {}
        for memoryLine in f:
            splittedMemories = memoryLine.split('=')
            myDict[splittedMemories[self.NAME_OF_MEMORY_INDEX]] = splittedMemories[self.VALUE_OF_MEMORY_INDEX]
        return myDict
    def say(self, sentence):
        print(sentence)

    def introduce(self):
        self.say("Hello I am " + str(self.myMemory.get("myName"))+" ! I was born on the " + str(self.myMemory.get("myBirthDate")))

    #return True to continue
    #return False to stop
    def hearUser(self):
        toAnalyze = input("Please send me a word : ")
        if str.lower(toAnalyze) == "stop":
            self.say("Ok, bye !")
            return False
        else:
            self.say("You said \""+toAnalyze+"\" but I did not understand. If you want to stop, just tell me STOP")
            return True
    def howDoYouFeel(self):
        self.say("For the moment...")
