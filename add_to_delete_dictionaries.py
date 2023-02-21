user_info={
    'name':'parth',
    'age':'19',
    'fav_movie':['avengers','kgf'],
    'fav_food':['dosa','vadapav'],
}
#how to add
user_info['fav_songs']=['song1','song2']
print(user_info)

#pop methode
user_items=user_info.pop('fav_movie')
print(user_info)

#popitems methode
user_items=user_info.popitem()
print(user_info)
print(type(user_info))
