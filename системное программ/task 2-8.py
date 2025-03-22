import math

class Calculator:
    def calculate_properties(self, radius):
        cir = 2 * math.pi * radius
        area = math.pi * radius**2
        return cir, area

calculator = Calculator()
radius = 3
cir, area = calculator.calculate_properties(radius)
print(f"Длина окружности = {cir:.2f}, площадь круга = {area:.2f}")