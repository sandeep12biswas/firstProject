from array import *


class Calc:

    def __init__(self, first=10, second=8):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second


calc = Calc()
calc.first = 9
calc.second = 6
sum = calc.add()

# print("sum = {}".format(sum))
print("Sum of the two numbers {} and {} is {}".format(calc.first, calc.second, sum))
