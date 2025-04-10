class NumberChecker:
    def __init__(self):
        self.numbers = []  

    def input_numbers(self, n):
        print(f"Введите {n} целых чисел:")
        for i in range(n):  
            number = int(input(f"Введите число c{i + 1}: "))
            self.numbers.append(number)

    def count_less_than_20(self):
        return sum(1 for number in self.numbers if number < 20)

    def check_condition(self):
        count = self.count_less_than_20()
        if count == 5:
            print("Количество чисел, меньших 20, равно пяти.")
        else:
            print(f"Количество чисел, меньших 20, не равно пяти. Оно равно {count}.")

n = int(input("Введите натуральное число n (количество чисел): "))
checker = NumberChecker()
checker.input_numbers(n)  
checker.check_condition()  