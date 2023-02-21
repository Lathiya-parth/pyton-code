# d=dict.fromkeys(['name','age'],'unkown')
# print(d)
#get methode usefull
d={'name':'parth','age':19}
# print(d['name'])
print(d.get('names'))

if 'name' in d:
    print('present')
else:
    print('not present')
    
if d.get('name'):
    print('present')
else:
    print('not present')
    
d.clear
print(d)

d1=d.copy
d1=d
print(d1.popitem())
print(d)
print(d1 is d)