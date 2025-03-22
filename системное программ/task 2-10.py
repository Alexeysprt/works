import math

class Calculator:
    def calculate_arithmetic(self, num1, num2):
         return (num1 + num2)/2
    
    def calculate_geometric(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return "Нельзя извлечь корень"
        return math.sqrt(num1 * num2)

calculator = Calculator()
num1 = 4
num2 = 8
print(f"а) Среднее арифметическое = {calculator.calculate_arithmetic(num1,num2)}")
print(f"б) Среднее геометрическое = {calculator.calculate_geometric(num1,num2)}")