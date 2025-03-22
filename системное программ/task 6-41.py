class Analyzer:
    def __init__(self, number):
        self.number = str(number)
    
    def max_digit(self):
        return max(self.number)
    
    def min_digit(self):
        return min(self.number)

number = int(input("Введите число: "))
analyzer = Analyzer(number)

max_digit = analyzer.max_digit()
min_digit = analyzer.min_digit()

print(f"Максимальная цифра: {max_digit}")
print(f"Минимальная цифра: {min_digit}")