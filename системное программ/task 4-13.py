class Material:
    def __init__(self, mass, volume):
        self.mass = mass 
        self.volume = volume 

    def density(self):
        return self.mass / self.volume

class DensityComparator:
    def __init__(self, material1, material2):
        self.material1 = material1  
        self.material2 = material2 

    def compare(self):
        density1 = self.material1.density()
        density2 = self.material2.density()

        if density1 > density2:
            print("Материал первого тела имеет большую плотность.")
        elif density1 < density2:
            print("Материал второго тела имеет большую плотность.")
        else:
            print("Плотности материалов обоих тел равны.")

print("Введите данные для первого тела:")
mass1 = float(input("Масса первого тела: "))
volume1 = float(input("Объем первого тела: "))

print("Введите данные для второго тела:")
mass2 = float(input("Масса второго тела: "))
volume2 = float(input("Объем второго тела: "))

material1 = Material(mass1, volume1)
material2 = Material(mass2, volume2)

comparator = DensityComparator(material1, material2)
comparator.compare()