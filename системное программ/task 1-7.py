import math

class EFormat:
    def __init__(self, value=math.e):
        self.value = value

    def format_e(self, places=1):
        formatvalue = f"{self.value:.{places}f}"
        return formatvalue

    def print_format_e(self, places=1):
        print(self.format_e(places))

E_format = EFormat()

E_format.print_format_e()