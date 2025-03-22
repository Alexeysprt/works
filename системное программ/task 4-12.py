class Area:
    def __init__(self, radius, lenght):
        self.lenght=lenght
        self.radius=radius
    def calc(self):
        self.circle = pow(self.radius,2)*3.14
        self.square = pow(self.lenght,2) 
        if self.circle > self.square:
            return print (f'circle more')
        else:
            return print (f'square more')

radius=int(input('enter lenght:'))
lenght=int(input('enter radius:'))
area = Area(radius, lenght)
area.calc()