age = int(input("Enter Your age: "))
#There will be a error when someone type the age in string (Ex: Twelve) 

if age >= 18:
    print(f"Yes! You can Drive the car at {age}.")
    

#The Correct Version is:

try:
    old = int(input("Enter You Age: "))
except ValueError:
    print("You have Type invalid input, Type again (Ex: age = 12, 21...)")
    old = int(input("Enter You Age:"))
    
if old >= 18:
    print(f"Yes! You can Drive the car at {old}.")