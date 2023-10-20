#a game of consequences
import random


woman = ["A scientist", "A queen", "A pirate", "A rabbit"]
man = ["a police", "an artist", "your grandfather, a killer robot"]
place = ["on pluto", "at the supermarket", "in the car"]
heWore = ["a purple suit", "a shark costume", "a beach towel"]
sheWore = ["scuba diving gear", "fairy wings", "a paper bag"]
womansays = ["'Who are you?", "'How many beans make five?", "'Why?"]
manSays = ["'Beep boop!", "'Don't eat frogs", "'What time do you call this?"]
consequence = ["world peace", "chaos", "a giant foot squashed them"]
worldSaid = ["'utter nonsense'", "'Cheese is trending now'", "'I\'m melting'"]

while True:
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("she was wearing", random.choice(sheWore))
    print("He was wearing", random.choice(heWore))
    print("she said", random.choice(womansays))
    print("he said", random.choice(manSays))
    print("The consequence was", random.choice(consequence))
    print("The world said", random.choice(worldSaid))
    print()
    input("press enter to play again")
    print()
