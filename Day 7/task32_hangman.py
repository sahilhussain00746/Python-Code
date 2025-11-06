import random
from task33_hangman_art import hangman_pic, hangman_logo
from task34_hangmanword import hangman_words

for line in hangman_logo:
    print(line)
    
random_word = random.choice(hangman_words) #creating random word 
print(random_word)

placeholder = "" #creating empty space
for position in range(len(random_word)): 
    placeholder += "_"
    
print(placeholder)

live = 6
game_over = False 
correct_letter = [] # creating a new list to store letter

while not game_over:  #running the loop while it is false
    
    guess = input("Enter a letter: ").lower() #taking input from user
    
    if guess in correct_letter:
        print(f"You have already guessed the letter {guess}")
        
    display = ""
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter) #putting the letter to remember and checking for another time when user gives the input
        elif letter in correct_letter: #checking the letter in available in the correct_list
            display += letter
        else:
            display += "_"
    
    print(display)
    
    if guess not in correct_letter:
        live -= 1
        print(f"You choose the wrong word {guess}")
        print(hangman_pic[live])
        if live == 0:
            game_over = True
            print("You lose")
        
    if "_" not in display:
        game_over = True
        print("You win")      
