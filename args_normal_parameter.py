def multiply_nums(num, *args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(2,4,2,3))