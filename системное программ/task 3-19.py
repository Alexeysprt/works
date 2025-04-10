class NumberProcessor:
    def __init__(self):
        self.number = 0  

    def input_number(self):
        while True:
            self.number = int(input("Введите трехзначное число: "))
            if 100 <= abs(self.number) <= 999:  
                break
            else:
                print("Ошибка: Введите трехзначное число.")

    def extract_digits(self):
        hundreds = abs(self.number) // 100  # Сотни
        tens = (abs(self.number) // 10) % 10  # Десятки
        units = abs(self.number) % 10  # Единицы
        return [hundreds, tens, units]

    def display_digits(self):
        digits = self.extract_digits()
        print(f"{digits[0]}, {digits[1]}, {digits[2]}")

processor = NumberProcessor()
processor.input_number()  
processor.display_digits()  