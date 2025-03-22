import math

class Calculator:
    def calculate_properties(self, edge):
        volume = edge**3
        area = 6 * edge**2
        return volume, area

calculator = Calculator()
edge = 4
volume, area = calculator.calculate_properties(edge)
print(f"Объем куба = {volume}, площадь поверхности = {area}")