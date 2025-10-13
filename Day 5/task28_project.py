print("Welcome to the Password Generator")

alphabet = [
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = [
"`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"
]

length_no = int(input("Entr the length of your password: "))
symbol_no = int(input("How many symbols should there: "))
numbers_no = int(input("How many numbers should there: "))

pass_list = [alphabet, number, symbols]

for doing in range(1, length_no):
    
