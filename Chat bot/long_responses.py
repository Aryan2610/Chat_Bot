import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what i want to ask!"
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
def nice():
    response = ["You are more fun than anyone or anything I know, including bubble wrap.",
                "You are the most perfect you there is",
                "You are enough.",
                "You just light up the room.",
                "I hope you are proud of yourself, because I am!"][
        random.randrange(5)]
    return response