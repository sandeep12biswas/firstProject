def divideNum():
    first_num = 10
    second_num = 2
    try:
        output = first_num / second_num
        print("Result = {}".format(output))
    except ZeroDivisionError as ex:
        print("Exception happened because {} is divided by {} and type of exception is {}".format(first_num,
                                                                                                  second_num,
                                                                                                  type(ex)))
    finally:
        print("Use greater than zero!")


class ExceptionHandle:
    pass


result = ExceptionHandle()
divideNum()
