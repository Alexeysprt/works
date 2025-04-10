class NumberAnalyzer:
    def __init__(self):  # Исправлено на двойные подчеркивания
        self.seq = []
        self.seq_finished = False

    def add_number(self, number):
        if number == 100:
            self.seq_finished = True
            return
        self.seq.append(number)

    def find_666_index(self):
        for i, value in enumerate(self.seq):
            if value == 666:
                return i + 1 
        return None

analyzer = NumberAnalyzer()

while not analyzer.seq_finished:
    num = int(input())
    analyzer.add_number(num)

result = analyzer.find_666_index()
print(result if result else "Число 666 не найдено")
