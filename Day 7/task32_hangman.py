hangman_pic= [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]




import random
word = ["lion", "tiger", "camel"]

random_word = random.choice(word) #creating random word 
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

    display = ""
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter) #putting the letter to remember and checking for another time when user gives the input
        elif letter in correct_letter: #checking the letter in available in the correct_list
            display += letter
        else:
            display += "_"
        
    if guess not in correct_letter:
        live -= 1
        if live == 0:
            game_over = True
            print("You lose")
        
    if "_" not in display:
        game_over = True
        print("You win")      
        
        
    print(hangman_pic[live])