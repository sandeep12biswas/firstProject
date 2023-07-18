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

def divideNum ():
    first_num = 10
    secnd_num = 3
    try:
        result = first_num/secnd_num;
        print("Result = {}".format(result))
    except ZeroDivisionError as ex :
        print("Exception happend because {} is devided by {} and type of exception is {}".format(first_num, secnd_num,type(ex)))
    finally:
        print("Use gretter than zero!")
devideNum()
