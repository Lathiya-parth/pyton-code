user_info={
    'name':'parth',
    'age':'19',
    'fav_movie':['avengers','kgf'],
    'fav_food':['dosa','vadapav'],
}

#check if key exit in dictionaries
if 'name' in  user_info:
    print('present')
else:
    print('not present')
    
#check if value exit in dictionaries
if 'parth' in  user_info.values():
    print('present')
else:
    print('not present')

#loop in dictionaries

for i in user_info.values():
    print(i)
for i in user_info:
    print(user_info[i])

#values methode
user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

#item methode

user_items=user_info.items()
print(user_items)
print(type(user_items))

for key,value in user_info.items():
    print(f"key is {key} and value is {value}")