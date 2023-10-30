from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides


    def roll_dice(self):
        for _ in range(10):
            print(randint(1, self.sides))


dice = Die()
#dice.roll_dice()

dice2 = Die(10)
#dice2.roll_dice()

dice2 = Die(20)
dice2.roll_dice()