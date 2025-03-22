import math

class Calculator:
    def calculate_function_1(self, a):
        return math.cos(a)
    
    def calculate_function_2(self, x):
      return  math.sin(x)/math.cos(x) if math.cos(x) != 0 else "Деление на 0"

calculator = Calculator()
print(f"a) f(a) = {calculator.calculate_function_1(math.pi / 2)}")
print(f"б) f(x) = {calculator.calculate_function_2(math.pi / 4)}")
--------------------------------------