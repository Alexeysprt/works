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

    def swap_second_and_third_digits(self):
        hundreds = abs(self.number) // 100  
        tens = (abs(self.number) // 10) % 10  
        units = abs(self.number) % 10  

        new_number = hundreds * 100 + units * 10 + tens

        return new_number if self.number > 0 else -new_number

    def display_result(self):
        result = self.swap_second_and_third_digits()
        print(f"Число после перестановки второй и третьей цифр: {result}")

manipulator = NumberManipulator()
manipulator.input_number()  
manipulator.display_result()  