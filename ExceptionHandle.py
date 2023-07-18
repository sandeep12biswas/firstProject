
class ExceptionsHandleMain:

    def __init__(self):
        self.second_num = None
        self.first_num = None

    def divideNum (self):

        self.first_num = input("Please enter first number : ")
        self.second_num = input("Please enter Second number : ")
        o = None
        try:
            o = int(self.first_num) / int(self.second_num)
        except ValueError as ve:
            print("Please enter valid number, {} and/or {} are/is not number".format(self.first_num,self.second_num))

        except ZeroDivisionError as ex:
            print("Exception happened because {} is divided by {} and type of exception is {}".format(self.first_num,
                                                                                                      self.second_num,
                                                                                                      type(ex)))
        finally:
            print("Use greater than zero!")

        return o


result = ExceptionsHandleMain()
output = result.divideNum()
print("Result = {}".format(output))
