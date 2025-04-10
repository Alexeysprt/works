class Cargo:
    def __init__(self):
        self.items = []  

    def input_masses(self):
        num_items = int(input("Введите количество предметов: "))
        print(f"Введите массы {num_items} предметов:")
        for i in range(num_items):  
            mass = float(input(f"Введите массу предмета {i + 1}: "))
            self.items.append(mass)

    def calculate_total_mass(self):
        return sum(self.items)

    def display_result(self):
        total_mass = self.calculate_total_mass()
        print(f"Общая масса груза: {total_mass}")

cargo = Cargo()
cargo.input_masses() 
cargo.display_result()  