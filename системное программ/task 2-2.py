import math

class Calculator:
    def calculate_function(self, a):
        return (2*a + math.sqrt(a))/(2*a - math.sqrt(a)) if 2*a - math.sqrt(a) !=0 else "Деление на 0"

calculator = Calculator()
print(f"y = {calculator.calculate_function(5)}")