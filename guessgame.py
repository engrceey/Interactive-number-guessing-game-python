# importing randint from random to generate the system guess
from random import randint

print("Welcome To an Interractive Number Guessing Game!!")


# Function for playing easy level
def easy():
    print("Welcome to Easy Level")
    sysGuess = randint(1, 10)
    for i in range(6):
        guesses = 5-i
        while True:
            try:
                userGuess = int(input("Guess a number from 1 to 10: "))
                if userGuess < 1 or userGuess > 10:
                    print("Guess is Out of Range!")
                    userGuess = int(input("Guess a number from 1 to 10: "))
                    continue
                else:
                    break
            except ValueError:
                print("Please Enter a number")
                continue
        if userGuess == sysGuess:
            print("WOW! YOU GOT IT!!!")
            break
        elif userGuess != sysGuess:
            print("That was wrong")
        print("You have %d guesses left" % guesses)
        if guesses == 0:
            print("GAME OVER!!")
            break
        if userGuess > sysGuess:
            print("Try a lower number")
        else:
            print("Try a higher number")


# Function for playing medium level
def medium():
    print("Welcome to Medium Level")
    sysGuess = randint(1, 20)
    for i in range(4):
        guesses = 3-i
        while True:
            try:
                userGuess = int(input("Guess a number from 1 to 20: "))
                if userGuess < 1 or userGuess > 20:
                    print("Guess is Out of Range!")
                    userGuess = int(input("Guess a number from 1 to 20: "))
                    continue
                else:
                    break
            except ValueError:
                print("Please Enter a number")
                continue
        if userGuess == sysGuess:
            print("WOW! YOU GOT IT!!!")
            break
        elif userGuess != sysGuess:
            print("That was wrong")
            print("You have %d guesses left" % guesses)
            if guesses == 0:
                print("GAME OVER!!")
                break
            if userGuess > sysGuess:
                print("Try a lower number")
            else:
                print("Try a higher number")


# function for playing Hard Level
def hard():
    print("Welcome to Hard Level")
    sysGuess = randint(1, 50)
    for i in range(3):
        guesses = 2-i
        while True:
            try:
                userGuess = int(input("Guess a number from 1 to 50: "))
                if userGuess < 1 or userGuess > 50:
                    print("Guess is Out of Range!")
                    userGuess = int(input("Guess a number from 1 to 50: "))
                    continue
                else:
                    break
            except ValueError:
                print("Please Enter a number")
                continue
        if userGuess == sysGuess:
            print("WOW! YOU GOT IT!!!")
            break
        elif userGuess != sysGuess:
            print("That was wrong")
            print("You have %d guesses left" % guesses)
            if guesses == 0:
                print("GAME OVER!!")
                break
            if userGuess > sysGuess:
                print("Try a lower number")
            else:
                print("Try a higher number")


# Function for selecting a level and validating user input
def selectLevel():
    userLevel = str(input("CHOOSE A LEVEL\nType Easy for Easy Level\nType Medium for Medium Level\nType Hard for Hard Level\n: "))
    while userLevel.lower() not in ("easyhardmedium"):
        print("INCORRECT INPUT! Try Again!")
        selectLevel()
    if userLevel.lower() == "easy":
        return easy()
    elif userLevel.lower() == "medium":
        return medium()
    elif userLevel.lower() == "hard":
        return hard()
selectLevel()