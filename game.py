#
# Filename: game.py
# Description: This implements the functions for the number guessing game.
# Author: Justin Luo
# Created: 3/6/2023
# Last Updated: 3/11/2023
# Version: 1.0
#
import random

def generate_number(x, y):
    '''
    inputs: x, y (range of numbers to be guessed)
    outputs: z (random number between x and y)
    this function is generating a random number between x and y.
    '''
    z = random.randint(x, y)
    return z

def get_guess(x, y):
    '''
    inputs: x, y 
    outputs: p (the user's guess)
    this function is taking the user's guess and outputting it.
    '''
    p = str(input("Guess a number between " + x + " and " + y + " "))
    return p

def check_guess(p, z):
    '''
    inputs: p (user's guess), z (original number)
    outputs: Too high!, Too low!, or Correct! 
    this function is checking if the user's guess and the original number are the same. 
    If they are, it returns correct, and if it isn't, it returns either too high or too low.
    '''
    if p > z:
        return "Too high!"
    elif p < z:
        return "Too low!"
    else:
        return "Correct!"
    
def play_game():
    '''
    inputs: none 
    outputs: none 
    this function takes all the previous functions together and structures the game. 
    This is what is running in the main.py file.
    '''
    print("Welcome to the number guessing game!")
    x = int(input("Choose the first whole number of your range: "))
    y = int(input("Choose your second whole number: "))
    attempts = int(input("How many attempts would you like? "))
    if attempts <= 0:
        print("You can't have that many attempts.")
        exit(0)
    g = ""
    while True:
        z = generate_number(x, y)
        while True:
            p = get_guess(str(x), str(y))
            c = check_guess(int(p), z)
            print(c)
            if c == "Correct!":
                g = input("Go again? y/n ")
                if g == "y":
                    break
                else:
                    exit(0)
            elif check_guess == "Too high!":
                attempts -= 1
                print("You have " + str(attempts) + " attempts.")
            else:
                attempts -= 1
                print("You have " + str(attempts) + " attempts.")
            if attempts <= 0:
                print("You lost.")
                print("The answer was " + str(z) + "." )
                exit(0)

play_game()
            
    