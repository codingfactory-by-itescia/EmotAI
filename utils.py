import random

def react_with_random(responses, count):
    if count >= len(responses):
        return responses[random.randint(0, len(responses) - 1)]
    return responses[count]


def react(responses, count):
    if count >= len(responses):
        return responses[len(responses) - 1]
    return responses[count]