#generate lists with range function
#somthing more about pop methode
#index methode
#pass list to a function

# numbers=list(range(1,11))
numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers)
# popped_item=numbers.pop()
# print(numbers)
# print(numbers.index(1,11,14))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    print(negative_list(numbers))