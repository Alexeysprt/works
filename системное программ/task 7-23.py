class Checker:
    def __init__(self, numbers):
        self.numbers = numbers

    def check_product(self, limit):
        product = 1
        for num in self.numbers:
            product *= num
            if product >= limit:
                return False
        return True

a1 = float(input("Введите число a1: "))
a2 = float(input("Введите число a2: "))
a3 = float(input("Введите число a3: "))
a4 = float(input("Введите число a4: "))
a5 = float(input("Введите число a5: "))
a6 = float(input("Введите число a6: "))
a7 = float(input("Введите число a7: "))
a8 = float(input("Введите число a8: "))

numbers = [a1, a2, a3, a4, a5, a6, a7, a8]

checker = Checker(numbers)
limit = 10000
result = checker.check_product(limit)

if result:
    print("Произведение меньше 10 000.")
else:
    print("Произведение больше или равно 10 000.")