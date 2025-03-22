class House:
    def __init__(self):
        self.floors = 9
        self.per_floor = 6
        self.entrances = 4

    def get_entrance(self, number):
        return (number - 1) // (self.floors * self.per_floor) + 1

    def get_floor(self, number):
        entrance_offset = (self.get_entrance(number) - 1) * self.floors * self.per_floor
        return ((number - 1 - entrance_offset) // self.per_floor) % self.floors + 1

    def get_on_floor(self, number):
        entrance_offset = (self.get_entrance(number) - 1) * self.floors * self.per_floor
        return (number - 1 - entrance_offset) % self.per_floor + 1

house = House()
number = int(input("Введите номер квартиры: "))
print(f"Въезд: {house.get_entrance(number)}")
print(f"Этаж: {house.get_floor(number)}")
print(f"Квартира на этаже: {house.get_on_floor(number)}")