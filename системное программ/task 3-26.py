class NumberPermutator:
    def __init__(self):
        self.number = 0  

    def input_number(self):
        while True:
            self.number = int(input("Введите трехзначное число с различными цифрами: "))
            if 100 <= abs(self.number) <= 999:  
                digits = set(str(abs(self.number)))  
                if len(digits) == 3:  
                    break
                else:
                    print("Ошибка: Все цифры числа должны быть различны.")
            else:
                print("Ошибка: Введите трехзначное число.")

    def generate_permutations(self):
        hundreds = abs(self.number) // 100  
        tens = (abs(self.number) // 10) % 10 
        units = abs(self.number) % 10  

        permutations = [
            hundreds * 100 + tens * 10 + units,
            hundreds * 100 + units * 10 + tens,
            tens * 100 + hundreds * 10 + units,
            tens * 100 + units * 10 + hundreds,
            units * 100 + hundreds * 10 + tens,
            units * 100 + tens * 10 + hundreds
        ]

        return [perm if self.number > 0 else -perm for perm in permutations]

    def display_result(self):
        permutations = self.generate_permutations()
        print("Шесть чисел, образованных при перестановке цифр:")
        print(", ".join(map(str, permutations)))

permutator = NumberPermutator()
permutator.input_number()  # Ввод числа
permutator.display_result()  # Вывод результата