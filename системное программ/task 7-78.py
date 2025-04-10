class PhysicsScore:
    def __init__(self, score):
        self.score = score

    def check_score(self):
        check_score = []
        for score in self.score:
            if 2 <= score <= 5:  
                check_score.append(score)
        self.score = check_score

    def count_score(self):
        counts = {5: 0, 4: 0, 3: 0, 2: 0}
        for score in self.score:
            counts[score] += 1
        return counts

score_list = [5, 4, 4, 5, 2, 2, 3, 3, 3, 5, 5, 4, 2, 2, 4 ]  

physics_score = PhysicsScore(score_list)
physics_score.check_score()  
result = physics_score.counts_score()  

print("Количество пятерок:", result[5])
print("Количество четверок:", result[4])
print("Количество троек:", result[3])
print("Количество двоек:", result[2])