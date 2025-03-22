class Analyzer:
    def __init__(self, number):
        self.number = str(number)

    def max_digit(self):
        odd_digits = [int(digit) for digit in self.number if int(digit) % 2 != 0]
        return max(odd_digits) if odd_digits else None

    def index_min_digit(self):
        min_digit = min(self.number)
        return self.number.index(min_digit)



number = input("Введите натуральное число: ")
analyzer = Analyzer(number)

max_odd_digit = analyzer.max_digit()
if max_odd_digit is not None:
    print(f"Максимальная нечетная цифра: {max_odd_digit}")
else:
    print("Нет нечетных цифр")

min_index = analyzer.index_min_digit()
print(f"Номер минимальной цифры (слева направо): {min_index + 1}")