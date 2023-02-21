s={1,2,3,4,5}
# print(s)
l=[1,2,3,4,5,5,5,5,6,7,7]
# s2=set(l)
s2=list(set(l))
print(s2)

s3={1,2,3}
s3.add(4) 
s3.add(5)
s3.add(4)
s3.remove(5)
s3.discard(4)
# s3=s.copy()
print(s3)

s4={1,1.0,1.1,2,'string'}
print(s4)