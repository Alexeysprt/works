import math

class Calculator:
    def calculate_perimeter(self, side):
        return 4 * side

calculator = Calculator()
print(f"Периметр квадрата = {calculator.calculate_perimeter(5)}")