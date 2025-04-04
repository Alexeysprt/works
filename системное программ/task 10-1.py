import random
class RandomNumber:
    def __init__(self):
        pass

    def generate_random_floats(self, count, lower_bound, upper_bound):
        return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

    def generate_random_natural(self, max_value):
        return random.randint(1, max_value)

    def task_a(self):
        numbers = self.generate_random_floats(8, 0, 1)
        print("а) 8 случайных вещественных чисел (0 ≤ ni < 1):")
        print(numbers)

    def task_b(self):
        k = int(input("Введите значение k: "))
        numbers = self.generate_random_floats(k, 0, 1)
        print(f"б) {k} случайных вещественных чисел (0 ≤ ni < 1):")
        print(numbers)

    def task_c(self):
        numbers = self.generate_random_floats(15, 25, 26)
        print("в) 15 случайных вещественных чисел (25 ≤ ni < 26):")
        print(numbers)

    def task_d(self):
        numbers = self.generate_random_floats(20, 0, 15)
        print("г) 20 случайных вещественных чисел (0 ≤ ni < 15):")
        print(numbers)

    def task_e(self):
        a = int(input("Введите значение a: "))
        b = float(input("Введите значение b: "))
        k = self.generate_random_natural(a)
        numbers = self.generate_random_floats(k, 0, b)
        print(f"д) Случайное натуральное число k = {k}, и {k} случайных вещественных чисел (0 ≤ ni < {b}):")
        print(numbers)

    def task_f(self):
        numbers = self.generate_random_floats(10, -40, 40)
        print("е) 10 случайных вещественных чисел (-40 ≤ ni < 40):")
        print(numbers)

    def task_g(self):
        m = int(input("Введите значение m: "))
        a = float(input("Введите значение a: "))
        b = float(input("Введите значение b: "))
        k = self.generate_random_natural(m)
        numbers = self.generate_random_floats(k, a, b)
        print(f"ж) Случайное натуральное число k = {k}, и {k} случайных вещественных чисел ({a} ≤ ni < {b}):")
        print(numbers)

rng = RandomNumber()
rng.task_a()
rng.task_b()
rng.task_c()
rng.task_d()
rng.task_e()
rng.task_f()
rng.task_g()