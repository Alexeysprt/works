class NumberHandler:
    def __init__(self):
        self.number = None

    def get_number(self):
        user_input = input("Введите число: ")
        self.number = float(user_input)

    def display_number(self):
        if self.number is not None:
            print(f"Ввели число {self.number}")
        else:
            print("Число не введено.")

handler = NumberHandler()

handler.get_number()

handler.display_number()