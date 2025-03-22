import math

class Calculator:
    def calculate_function_1(self, x, y):
        return 2 * x**3 - 3.44 * x * y + 2.3 * x**2 - 7.1 * y + 2
    
    def calculate_function_2(self, a, b):
         return 3.14 * (a + b)**3 + 2.75 * b**2 - 12.7 * a - 4.1

calculator = Calculator()
print(f"a) z = {calculator.calculate_function_1(2, 3)}")
print(f"б) x = {calculator.calculate_function_2(1, 2):.2f}")