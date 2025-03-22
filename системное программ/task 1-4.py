class NumberPrinter:
    def __init__(self, *numbers):
        self.numbers = numbers

    def printnum(self):
        for number in self.numbers:
            print(number)

printer = NumberPrinter(5, 10, 21)

printer.printnum()