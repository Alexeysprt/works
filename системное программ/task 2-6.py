import math

class Calculator:
    def calculate_distance(self, height, earth_radius=6350):
        if height < 0:
            return "Высота не может быть отрицательной"
        return math.sqrt(2 * earth_radius * height + height**2)

calculator = Calculator()
height = 100
print(f" Расстояние до горизонта = {calculator.calculate_distance(height):.2f} км")