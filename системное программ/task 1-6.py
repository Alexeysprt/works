import math

class PiFormat:
    def __init__(self, value=math.pi):
        self.value = value

    def format_pi(self, places=3):
        formatvalue = f"{self.value:.{places}f}"
        return formatvalue

    def print_format_pi(self, places=3):
        print(self.format_pi(places))

pi_format = PiFormat()

pi_format.print_format_pi()