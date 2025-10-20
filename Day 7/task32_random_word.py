import random
word = ["lion", "tiger", "camel"]

random_word = random.choice(word)
print(random_word)

guess = input("Enter a letter: ").lower()

guess_no = 0
for letter in random_word:
    if guess == letter:
        guess_no = 1

if(guess_no == 1):
    print("Correct letter")
else: 
    print("Wrong letter")