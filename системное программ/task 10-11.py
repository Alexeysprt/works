import random

class Dice:
    def __init__(self):
        pass

    def roll(self):
        return random.randint(1, 6)

    def simulate(self):
        result = self.roll()
        print(f"Результат броска кубика: {result}")

dice = Dice()
dice.simulate()