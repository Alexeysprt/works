class Apples:
    def __init__(self, students, apples):
        self.students = students
        self.apples = apples

    def apples_student(self):
        return self.apples // self.students
    def remain(self):
        return self.apples % self.students

def main():
    students = int(input("Введите количество школьников: "))
    apples = int(input("Введите количество яблок: "))
    if students <= 0 or apples <= 0:
        print("Количество школьников и яблок должны быть положительными числами!")
        return

    dis = Apples(students, apples)
    apples_student = dis.apples_student()
    remain = dis.remain()
    print(f"Каждому школьнику достанется {apples_student} яблок.")
    print(f"В корзинке останется {remain} яблок.")
    
main()