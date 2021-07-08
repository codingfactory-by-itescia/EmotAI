import json

class PersonalityParser:
    @staticmethod
    def parse(personality_file_name):
        file = open("./personalities/" + personality_file_name + ".json")
        return json.loads(file.read())

    @staticmethod
    def save(personality_file_name, values):
        file = open("./personalities/" + personality_file_name + ".json", "w")
        json_values = json.dumps(values, indent=4)
        file.write(json_values)
        file.close()
