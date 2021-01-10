from random import randint
from art import logo

EASY = 10
HARD = 5
   
#Choosing a random number between 1 and 100
print(logo) 
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

#guess a number
guess=int(input("Make a guess: \n"))



# Check user's guess against actual answer.
def check_answer(guess, answer):
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print(f"You got it. The answer is {answer}")


def level():
    guess = input("Make a guess: \n")



difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
if input == "easy":
    print(f"You have 10 attempts remaining to guess the number")
else:
    print(f"You have 5 attempts remaining to guess the number")


