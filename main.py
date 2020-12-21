rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
image = [rock, paper, scissors]
user_choice = int(input("0 for rock, 1 for paper, 2 for scissors. \n"))
print(image[user_choice])
computer_choice = random.randint(0, 2)
print(computer_choice)
print(image[computer_choice])

if user_choice > 2 or user_choice < 0:
  print("invalid number please try again")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print ("You loose!")
elif user_choice > computer_choice:
  print ("You win!")
elif computer_choice < user_choice:
  print("You loose!")
else:
  print("it's draw")
 
