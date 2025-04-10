class NumberSum:
    def __init__(self):
        self.numbers = [] 

    def input_numbers(self, n):
        print(f"Введите {n} вещественных чисел:")
        for i in range(n):  # Вводим n чисел
            number = float(input(f"Введите число a{i + 1}: "))
            self.numbers.append(number)

    def calculate_sum(self):
        return sum(self.numbers)

    def display_result(self):
        total_sum = self.calculate_sum()
        print(f"Сумма всех вещественных чисел: {total_sum}")

n = int(input("Введите натуральное число n (количество чисел): "))
calculator = NumberSum()
calculator.input_numbers(n)  
calculator.display_result()  