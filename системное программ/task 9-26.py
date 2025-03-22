class Finder:
    def __init__(self):
        self.primes = []  

    def is_prime(self, number):
        
        if number < 2:
            return False
        for divisor in range(2, int(number**0.5) + 1): 
            if number % divisor == 0:
                return False
        return True

    def find_first_100(self):
        
        candidate = 2  
        while len(self.primes) < 100:  
            if self.is_prime(candidate): 
                self.primes.append(candidate)  
            candidate += 1 

    def print_primes(self):
        print("Первые 100 простых чисел:")
        print(self.primes)

finder = Finder()
finder.find_first_100()
finder.print_primes()