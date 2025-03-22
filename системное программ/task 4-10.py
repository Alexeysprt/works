class Distance:
    def __init__(self, kilometer, foot):
        self.kilometer=kilometer
        self.foot=foot
    def calc(self):
        self.foot = self.foot * 0.3048
        self.kilometer = self.kilometer * 1000
        if self.kilometer > self.foot:
            return print (f'km more')
        else:
            return print (f'ft more')

km=int(input('enter km:'))
ft=int(input('enter ft:'))
distance = Distance(km, ft)
distance.calc()