class EvenNumbersProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_even(self, number):
        return (number % 2 == 0) * number
    def sum_of_evens(self):
        total = 0
        for num in self.numbers:
            total += self.is_even(num)
        return total


numbers = []
print("Введите 10 целых чисел по одному:")
for i in range(10):
    number = int(input(f"Число {i + 1}: "))
    numbers.append(number)

processor = EvenNumbersProcessor(numbers)
result = processor.sum_of_evens()
print("Сумма четных чисел:", result)