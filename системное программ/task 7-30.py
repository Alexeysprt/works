class Calculator:
    def __init__(self, masses):
        self.masses = masses

    def average_mass(self):
        total_mass = sum(self.masses)
        average_mass = total_mass / len(self.masses)
        return average_mass

masses = [30, 27, 9, 22, 42] 
calculator = Calculator(masses)
average_mass = calculator.average_mass()

print(f"Средняя масса: {average_mass:}")