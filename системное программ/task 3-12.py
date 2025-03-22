class flats:
    def __init__(self, total=5, per_floor=4):
        self.total = total
        self.per_floor = per_floor
        
    def get_floor(self, number):
        return (number - 1) // self.per_floor + 1
    
    def position(self, number):
        return (number - 1) % self.per_floor + 1

finder = flats()
apartment_number = int(input("Введите номер квартиры: "))
floor = finder.get_floor(apartment_number)
position = finder.position(apartment_number)
print(f"Квартира {apartment_number} находится на {floor}-м этаже.")
print(f"Порядковый номер этой квартиры на этаже: {position}.")