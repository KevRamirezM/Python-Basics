#Number guessing game

import random

lowestnum = 1
highestnum = 100
answer = random.randint(lowestnum, highestnum)
guesses = 0

is_running = True

print("Welcome to Python Number Guessing Game")

print(f"Select a number between {lowestnum} and {highestnum}")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowestnum or guess > highestnum:
            print("That number is out of range")
            print(f"Please select a number between {lowestnum} and {highestnum}")
        
        elif guess < answer :
            print("Too low! Try Again...")
        
        elif guess > answer:
            print("Too high! Try again...")
        
        else:
            print(f"Correct! The answer was: {answer}")
            print(f"Number of Guesses: {guesses}")
            is_running = False
            
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowestnum} and {highestnum}")


