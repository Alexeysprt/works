class NumberFinder:
    def __init__(self, a):
        self.a = a  
        self.n = 2  

    def find_first(self):
        while True:
            number = 1 + 1 / self.n 
            if number < self.a: 
                return number
            self.n += 1  



a = 1.2  
finder = NumberFinder(a)
result = finder.find_first()
print(f"Первое число, меньшее {a}: {result}")