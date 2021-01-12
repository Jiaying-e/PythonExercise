import random
from art import logo, vs
from replit import clear
from game_data import data
random_b = random.choice(data)

def format_data(entry):
    """Format the data,name, description, country"""
    new_name = entry['name']
    new_description = entry['description']
    new_country = entry['country']

    return f"{new_name}, a {new_description}, from {new_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess against the follower countand return if they got it right"""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

#display art
print(logo)
score = 0
game_continue = True

#Make the game repeatable
while game_continue:

    #Generate a random entry
    random_a = random_b
    random_b = random.choice(data)
    while random_a == random_b:
        random_b = random.choice(data)

    print(f"Compare A: {format_data(random_a)}")
    print(vs)
    print(f"Against B: {format_data(random_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? 'A' or 'B'?").upper()

    #Check if user is correct, get follower_count
    a_followers_count=random_a['follower_count']
    b_followers_count = random_b['follower_count']
    print(a_followers_count)
    print(b_followers_count)

    correct = check_answer(guess, a_followers_count, b_followers_count)

    #Clear the screen between rounds
    clear()
    print(logo)
    #Print you are right or you are wrong
    #count the score
    if correct:
        score = score + 1
        print(f"You are right, and your score is {score}")
    else:
        game_continue = False
        print(f"Sorry, and you final score: {score}")





