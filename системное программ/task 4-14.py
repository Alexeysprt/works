class CircuitSegment:
    def __init__(self, resist, volt):
        self.resist = resist 
        self.volt = volt  

    def current(self):
        return self.volt / self.resist


class CurrentComparator:
    def __init__(self, segment1, segment2):
        self.segment1 = segment1  
        self.segment2 = segment2  

    def compare(self):
        current1 = self.segment1.current()
        current2 = self.segment2.current()

        if current1 < current2:
            print("Меньший ток протекает по первому участку.")
        elif current1 > current2:
            print("Меньший ток протекает по второму участку.")
        else:
            print("Токи на обоих участках равны.")

print("Введите данные для первого участка:")
resist1 = float(input("Сопротивление первого участка: "))
volt1 = float(input("Напряжение на первом участке: "))

print("Введите данные для второго участка:")
resist2 = float(input("Сопротивление второго участка: "))
volt2 = float(input("Напряжение на втором участке: "))

segment1 = CircuitSegment(resist1, volt1)
segment2 = CircuitSegment(resist2, volt2)

comparator = CurrentComparator(segment1, segment2)
comparator.compare()