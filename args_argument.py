def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply
num=[1,2,3]
print(multiply_nums(*num))
