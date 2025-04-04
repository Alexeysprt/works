import random

class Coin:
    def __init__(self):
        pass

    def toss(self):
        return random.randint(0, 1)

    def simulate_toss(self):
        result = self.toss()
        if result == 0:
            print("Результат подбрасывания монеты: Орел")
        else:
            print("Результат подбрасывания монеты: Решка")

coin = Coin()
coin.simulate_toss()