number=list(range(1,11))
num=[]
for i in number:
    if i%2==0:
        num.append(i)
print(num)


even_nums=[i for i in number if i%2==0]
even_nums2=[i for i in range(1,11) if i%2==0]
print(even_nums)
print(even_nums2)
odd_nums=[i for i in range(1,11) if i%2!=0]
print(odd_nums)