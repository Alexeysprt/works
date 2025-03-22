class Finder:
    def __init__(self, n):
        self.n = n 
        self.k = 1  
        self.current_sum = 0 

    def find_first(self):
        while True:
            self.current_sum += 1 / self.k 
            if self.current_sum > self.n:
                return self.current_sum
            self.k += 1

n = 9
finder = Finder(n)
result = finder.find_first()
print(f"Первое число, большее {n}: {result}")