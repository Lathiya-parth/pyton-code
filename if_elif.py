age=input("enter your age:")
age=int(age)
if age==0  or age<0:
    print("you can't watch")
elif 0<age<=3:
    print("your ticket:free")
elif 3<age<=10:
    print("your ticket:150")
elif 10<age<=60:
    print("your ticket:250")
else:
    print("your ticket:200")        