user={}
name=input('what is your name')
age=input('what is your age')
fav_movie=input('ypur fav sepreted movie comma ').split(",")
fav_song=input('ypur fav sepreted song comma ').split(",")

user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_song']=fav_song
# print(user)
  
for key,value in user.items():
    print(f"{key}:{value}")