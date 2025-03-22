class Speed:
    def __init__(self, mps, kmph):
        self.kmph=kmph
        self.mps=mps
    def calc(self):
        self.mps = self.mps
        self.kmph = self.kmph / 3.6
        if self.kmph > self.mps:
            return print (f'kmph more')
        else:
            return print (f'mps more')

kmph=int(input('enter kmph:'))
mps=int(input('enter mps:'))
speed = Speed(kmph, mps)
speed.calc()