class Numbers:
    def __init__(self, number):
        self.number = str(number)

    def move(self):
        return int(self.number[-1] + self.number[:-1])


number = input("Введите трехзначное число: ")
numbers = Numbers(number)
result = numbers.move()
print(f"Полученное число: {result}")
