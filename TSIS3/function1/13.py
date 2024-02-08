import random

def programm():
    print("Hello, what is your name?")
    userName = str(input())
    print(f"Well, {userName}, I am thinking of a number between 1 and 20. \n Take a guess.")

    i = 1
    flag = True
    programmGuess = random.randint(1,20)
    while(flag):
        userGuess = int(input())
        if(userGuess == programmGuess): 
            flag = False
            return print(f"Good job, {userName}! You guessed my number in {i} guesses!")
        if(userGuess < programmGuess):
            print("Your guess is too low. \n Take a guess.")
        else:
            print("Your guess is too high. \n Take a guess.")
        i = i + 1
programm()