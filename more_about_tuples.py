#for loop and tuple
mixed=(1,2,3,5.2)

for i in mixed:
    print(i)
    
#tuples with one element
nums=('1',) 
word=('word1',)
print(type(nums))
print(type(word))

#tuples with parenthesis

guiter='parth','lathiya','farmer'
print(type(guiter))


#tuple unpacking
guiterists=('parth','ravi','prince')
guiterists1,guiterists2,guiterists3=guiterists
print(guiterists1)

#list inside tuples
favorites=('parth',['rushit','ravi'])
favorites[1].pop()
favorites[1].append("prince")
print(favorites)


#min(),max,sum

print(sum(mixed))