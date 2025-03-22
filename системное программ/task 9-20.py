class DivisibilityGraph:
    def __init__(self):
        self.n = 0  

    def input_n(self):
        while True:
            user_input = input("Введите число n (n >= 1): ")
            if user_input.isdigit() and int(user_input) >= 1:
                self.n = int(user_input)
                break
            else:
                print("Число должно быть целым и больше или равно 1.")

    def count_divisors(self, number):
        divisors_count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                divisors_count += 1
        return divisors_count

    def print_divisibility(self):
        for number in range(1, self.n + 1):  
            divisors_count = self.count_divisors(number)  
            print(f"{number}{'+' * divisors_count}")  

graph = DivisibilityGraph()
graph.input_n() 
graph.print_divisibility()  