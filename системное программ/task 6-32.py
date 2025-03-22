class Runner:
    def __init__(self):
        self.start = 10
        self.daily_increase = 0.1

    def daily_distance(self, day):
        if day == 1:
            return self.start
        else:
            return self.daily_distance(day - 1) * (1 + self.daily_increase)

    def sum_distance(self, day):
        if day == 1:
            return self.start
        else:
            return self.sum_distance(day - 1) + self.daily_distance(day)

    def find_day(self, limit, type='daily'):
        day = 1
        while True:
            if type == 'daily':
                distance = self.daily_distance(day)
            elif type == 'sum':
                distance = self.sum_distance(day)
            
            if distance > limit:
                return day
            day += 1


runner = Runner()

day_20km = runner.find_day(20, 'daily')
print(f"when 20 km {day_20km}.")

day_100km = runner.find_day(100, 'sum')
print(f"when 100km {day_100km}.")