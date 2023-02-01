def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else: 
       return c
print (greater(10,20,30))

# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# def new_greatest(a,b,c):
#      bigger=greater(a,b)
#      return greater(bigger,c)
  
# print(new_greatest(100,200,300))
     
    