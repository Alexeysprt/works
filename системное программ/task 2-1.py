import math

class Calculator:
    def calculate_function_1(self, x):
        return 17 * x**2 - 6 * x + 13

    def calculate_function_2(self, a):
        return 3 * a**2 + 5 * a - 21

calculator = Calculator()
print(f"a) y = {calculator.calculate_function_1(5)}")
print(f"б) y = {calculator.calculate_function_2(3)}")