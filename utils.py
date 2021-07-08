import random

def react_with_random(responses, count):
    if count >= len(responses):
        return responses[random.randint(0, len(responses) - 1)]
    return responses[count]


def react(responses, count):
    if count >= len(responses):
        return responses[len(responses) - 1]
    return responses[count]

def handle_reaction(emot_ai, table, action):
    emot_ai.say(
        react(
            table,
            emot_ai.actions_memory.count_value(action)
        )
    )
    emot_ai.actions_memory.add(action)

def handle_with_random_reaction(emot_ai, table, action):
    emot_ai.say(
        react_with_random(
            table,
            emot_ai.actions_memory.count_value(action)
        )
    )
    emot_ai.actions_memory.add(action)