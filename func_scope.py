x=5
def func():
  global x
  x=7
  return x
print(x)      #value change karva mate(5 change 7)
print(func())
print(x)