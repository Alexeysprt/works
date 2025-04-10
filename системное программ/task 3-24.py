class NumberManipulator:
    def __init__(self):
        self.number = 0  

    def input_number(self):
        while True:
            self.number = int(input("Введите трехзначное число: "))
            if 100 <= abs(self.number) <= 999:  
                break
            else:
                print("Ошибка: Введите трехзначное число.")

    def swap_first_and_second_digits(self):
        hundreds = abs(self.number) // 100  
        tens = (abs(self.number) // 10) % 10  
        units = abs(self.number) % 10  

        new_number = tens * 100 + hundreds * 10 + units

        return new_number if self.number > 0 else -new_number

    def display_result(self):
        result = self.swap_first_and_second_digits()
        print(f"Число после перестановки первой и второй цифр: {result}")

manipulator = NumberManipulator()
manipulator.input_number()  
manipulator.display_result()  