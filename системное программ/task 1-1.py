class Numbers:
    def __init__(self, *numbers):
        self.numbers = numbers

    def form_numbers(self):
        return ' '.join(map(str, self.numbers))

    def print_forma(self):
        print(self.form_numbers())

format = Numbers(31, 18, 79)

format.print_forma()