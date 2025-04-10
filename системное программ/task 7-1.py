class NumberSum:
    def __init__(self):
        self.numbers = []  

    def input_numbers(self):
        print("Введите 10 чисел:")
        for i in range(10):  
            number = float(input(f"Введите число a{i + 1}: "))
            self.numbers.append(number)

    def calculate_sum(self):
        return sum(self.numbers)

    def display_result(self):
        total_sum = self.calculate_sum()
        print(f"Сумма чисел: {total_sum}")

calculator = NumberSum()
calculator.input_numbers() 
calculator.display_result()