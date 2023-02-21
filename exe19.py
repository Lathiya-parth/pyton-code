def sublist_couter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
mixed=[1,2,3,[1,5,6],[5,6,7]]
print(sublist_couter(mixed))