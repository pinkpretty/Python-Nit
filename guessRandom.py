#Guess Random Number
#Generate a Random number between 0 to 9

import random

turn = 0
def guessRandom():
    secretNumber = random.randint(0,9)
    
guessNumber = int(input("Guess a Random number between 0-9"))
while secretNumber != guessNumber:
    if(secretNumber > guessNumber):
        input("You have Guessed the number higher than secretNumber. Guess Again!")
        turn = turn + 1
    elif (secretNumber < guessNumber):
        input("You have guessed the number lower than secretNumber. Guess Again! ")
        turn = turn + 1
if(secretNumber == guessNumber):
        print("you Have Guessed it Right!")
guessRandom()
