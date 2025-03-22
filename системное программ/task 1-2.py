class Numbers:
    def __init__(self, *numbers):
        self.numbers = numbers

    def form_numbers(self):
        return '  '.join(map(str, self.numbers))

    def print_forma(self):
        print(self.form_numbers())

format = Numbers(47, 52, 150)

format.print_forma()