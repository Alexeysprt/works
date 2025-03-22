class Rectangle:
    def __init__(self, square, rectangle):
        self.square = square
        self.rectangle = rectangle

    def find_square1(self):
        res1 = 543*130
        return res1
    def find_square2(self):
        res2 = 130*130
        return res2

def main():
    rect=Rectangle(square=130, rectangle=(543, 130))
    result1 = rect.find_square1()
    result2 = rect.find_square2()
    result3 = result1 // result2
    print(f'Результат: {result3}')
main()