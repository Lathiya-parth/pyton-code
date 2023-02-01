#neseted if else
winning_number=27
user_input=int(input("guess a nuber of 1/100:"))
if user_input == winning_number:
    print("you win!!!")
    
else:
    if user_input <winning_number:
        print("too law!!!")
    else:
         print("too high!!!")