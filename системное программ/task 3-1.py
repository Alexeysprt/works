class Distance:
    def __init__(self, cm):
        self.cm = cm

    def get_meters(self):
        meters = int(self.cm // 100)
        return meters

if __name__ == "__main__":
    while True:
        user_input = input("Введите расстояние в сантиметрах или 'q' для выхода: ")
        if user_input.lower() == 'q':
            print("Выход")
            break

        cm = float(user_input)
        distance = Distance(cm)
        meters = distance.get_meters()
        print(f"Количество полных метров: {meters}")