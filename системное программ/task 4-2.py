import math
class Equation:
    def __init__(self):
        pass

    def calc(self):
        user_input = float(input("Введите x: "))
        if user_input > 0:
            y = pow(math.sin(user_input), 2)
        else:
            y = 1 - 2 * math.sin(pow(user_input, 2))
        return y
equation = Equation()
result = equation.calc()
print(f"Результат вычисления: {result}")