import random, art
EASY_LEVEL = 10
HARD_LEVEL = 5 #these are the two constant

def num_checking(num, user_num):
    """Comparing the gussed number"""
    if num == user_num:
        print("You won!")
        return 0
        
    elif num > user_num:
        print("Wrong!, Number is LOW") 
        return 1
        
    elif num < user_num:
        print("Wrong! Number is High")
        return 1 

def diff_level():
    """Setting the difficulty level"""
    global EASY_LEVEL, HARD_LEVEL
    level = input("Choose your difficulty level 'easy' or 'hard': ").lower()
    if level == "easy":
        print("You have 10 lives")
        return EASY_LEVEL
    else: 
        print("You have 5 lives")
        return HARD_LEVEL

print(art.logo)
num = random.randint(1, 100)
print("Welcome to the number guessing game")
print("Think a number between 1 to 100")

user_level = diff_level()

    
should_continue = True
while should_continue:
    user_num = int(input("Enter Your Guessed number: "))
    after_check = num_checking(num, user_num)
        
    user_level -= after_check
    if after_check != 0:
        print(f"You have {user_level} lives left")
        
    if after_check == 0:
        should_continue = False   
    elif user_level == 0:
        print("You Lose!")
        print(f"The number was: {num}")
        should_continue = False
        