class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def abs_value(self, x):
        return (x + abs(x)) // 2 + (-x + abs(x)) // 2

    def sum_of_abs(self):
        total = 0
        for num in self.numbers:
            total += self.abs_value(num)
        return total

    def product_of_abs(self):
        product = 1
        for num in self.numbers:
            product *= self.abs_value(num)
        return product

    def sums_of_consecutive(self):
        sums = []
        for i in range(1, len(self.numbers)):
            sums.append(self.numbers[i - 1] + self.numbers[i])
        return sums



n = int(input("количество (n): "))
numbers = list(map(int, input("числа через пробел: ").split()))

calculator = Calculator (numbers)

print("1) Сумма модулей:", calculator.sum_of_abs())
print("2) Произведение модулей:", calculator.product_of_abs())
print("3) Суммы соседних элементов:", calculator.sums_of_consecutive())