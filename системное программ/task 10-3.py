import random

class RandomNumber:
    def __init__(self):
        pass

    def generate_random_natural(self, max_value):
        return random.randint(1, max_value)

    def generate_random_integers(self, count, lower_bound, upper_bound):
        return [random.randint(lower_bound, upper_bound) for _ in range(count)]

    def generate_random_floats(self, count, upper_bound):
        return [random.uniform(0, upper_bound) for _ in range(count)]

    def solve_task(self):
        a = int(input("Введите значение a: "))
        b = int(input("Введите значение b: "))

        m = self.generate_random_natural(20)
        n = self.generate_random_natural(20)
        random_integers = self.generate_random_integers(n, a, b)

        random_floats = self.generate_random_floats(m, n)

        print(f"Случайное натуральное число m: {m}")
        print(f"Случайное натуральное число n: {n}")
        print(f"{n} случайных целых чисел в диапазоне [{a}, {b}]:")
        print(random_integers)
        print(f"{m} неотрицательных случайных вещественных чисел, не превосходящих {n}:")
        print(random_floats)

rng = RandomNumber()
rng.solve_task()