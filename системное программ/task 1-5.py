class NumberPrinter:
    def __init__(self, *numbers):
        self.numbers = numbers

    def printnum(self):
        for number in self.numbers:
            print(number)

printer = NumberPrinter(1, 2)

printer.printnum()