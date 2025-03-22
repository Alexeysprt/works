class Train:
    def __init__(self, place, coupe):
        self.place = place
        self.coupe = coupe

    def find_coupe(self):
        res1 = 4*9
        return res1
    
def main():
    place = int(input("Введите место: "))
    if place >= 36:
        print("нет такого")
        return
    rect=Train(coupe=9, place=4)
    result1 = rect.find_coupe()
    result3 = place // 4+1
    print(f'Результат: {result3}')
main()