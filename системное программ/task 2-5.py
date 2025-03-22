import math

class Calculator:
    def calculate_diameter(self, radius):
       return 2 * radius

calculator = Calculator()
print(f"Диаметр окружности = {calculator.calculate_diameter(7)}")