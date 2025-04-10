class Polygon:
    def __init__(self):
        self.sides = []  

    def input_sides(self, num_sides):
        print(f"Введите длины {num_sides} сторон многоугольника:")
        for i in range(num_sides): 
            side = float(input(f"Введите длину стороны {i + 1}: "))
            self.sides.append(side)

    def calculate_perimeter(self):
        return sum(self.sides)

    def display_result(self):
        perimeter = self.calculate_perimeter()
        print(f"Периметр 12-угольника: {perimeter}")

polygon = Polygon()
polygon.input_sides(12) 
polygon.display_result() 