def game():
    for i in range(1, 20): #change range(1, 21) to fix this bug
        if i == 20:
            print("You got this!")
        
game()

# There is a bug in the for loop is that
# the loop will only runs till 19

#Another Example

year = int(input("What is your dob: "))

if year > 1980 and year < 1994: #There is a bug in the operator
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z")
    
# when the year is 1980 or 1994 then it print nothing
# year >= 1980 and year < 1994
# year >= 1994