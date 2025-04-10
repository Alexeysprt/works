class Pay:
    def __init__(self):
        self.salaries = []  

    def input_salaries(self):
        num_employees = int(input("Введите количество сотрудников: "))
        print(f"Введите зарплату для {num_employees} сотрудников:")
        for i in range(num_employees):  
            salary = float(input(f"Введите зарплату сотрудника {i + 1}: "))
            self.salaries.append(salary)

    def calculate_total_payment(self):
        return sum(self.salaries)

    def display_result(self):
        total_payment = self.calculate_total_payment()
        print(f"Общая сумма выплаченных денег: {total_payment}")

pay = Pay()
pay.input_salaries()  
pay.display_result()  