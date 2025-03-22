class Time:
    def __init__(self, days):
        self.days = days

    def get_week(self):
        week = int(self.days // 7)
        return week

if __name__ == "__main__":
    while True:
        user_input = input("Введите время в днях или 'q' для выхода: ")
        if user_input.lower() == 'q':
            print("Выход")
            break

        days = float(user_input)
        time = Time(days)
        week = time.get_week()
        print(f"Количество полных центнеров: {week}")