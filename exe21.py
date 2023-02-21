def reverse_string(l):
    return [name[::-1] for name in l]
print(reverse_string(['abc','pqr','xyz']))

def reverse_str(l):
    new_list=[]
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(reverse_str(['abc','pqr','xyz']))