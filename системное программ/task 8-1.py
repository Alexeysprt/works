class SquareGenerator:
    def __init__(self, n):
        self.n = n  
        self.current = 1  

    def generate_squares(self):
        
        while True:
            square = self.current ** 2  
            if square > self.n:  
                break
            print(square)  
            self.current += 1  



n = 10000 
generator = SquareGenerator(n)
generator.generate_squares()