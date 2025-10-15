import random

print("Welcome to the Password Generator")

alphabet = [
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
"`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"
]

length_no = int(input("Entr the length of your password: "))
symbol_no = int(input("How many symbols should there: "))
numbers_no = int(input("How many numbers should there: "))

# password = ""

# for doing in range(0, length_no):
#     password += random.choice(alphabet)

# for doing in range(0, symbol_no):
#     password += random.choice(symbols)

# for doing in range(0, numbers_no):
#     password += random.choice(str(number))
    
# print(password) #This will print the simple password in order

password_list = []

for doing in range(0, length_no):
    password_list.append(random.choice(alphabet))

for doing in range(0, symbol_no):
    password_list.append(random.choice(symbols))

for doing in range(0, numbers_no):
    password_list.append(random.choice(number))
    
print(password_list)
random.shuffle(password_list)
print(password_list)
 
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
