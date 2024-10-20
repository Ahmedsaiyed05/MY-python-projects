import random 
rn = random.randint(1,10)
print(rn)

userGuess= None 
guesses = 0 

while(userGuess !=rn ): 
    userGuess = int(input("guess the number : "))
    guesses += 1
    if(userGuess == rn):
        print("you guessed it right ! ")
    else : 
        if(userGuess>rn):
            print("you guessed it wrong enter the smaller number ")
        else:
            print("enter the larger number")
            