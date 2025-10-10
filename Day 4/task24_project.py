import random
#rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

group = [rock, scissors, paper]

user_input = int(input("Choose 0 for Rock, 1 for paper, 2 for scissors: \n"))
if user_input >=0 and user_input < 3:
    print("You Choose: \n" + group[user_input])

computer_input = random.randint(0, 2)
if user_input >=0 and user_input < 3:
    print("Computer Choose: \n" + group[computer_input])

if user_input >=3 or user_input < 0:
    print("You enterd a invalid choice, You lose")
elif user_input == 0:
    if computer_input ==1:
        print("You win")
    elif computer_input == 2:
        print("You lose")
    else:
        print("Match Draw")
        
elif user_input == 1:
    if computer_input ==2:
        print("You win")
    elif computer_input == 0:
        print("You lose")
    else:
        print("Match Draw")
        
elif user_input == 2:
    if computer_input ==1:
        print("You lose")
    elif computer_input == 0:
        print("You win")
    else:
        print("Match Draw")
        
    