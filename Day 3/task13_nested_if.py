print("Welcome to the rollar coaster")
height = float(input("What is your height: "))
age = int(input("Enter Your age: "))
bill = 0
if height>=120:
    if age<12:
        bill = 5;
        print(f"Child ticket price ${bill}")
    elif age<18:
        bill = 10;
        print(f"Youth ticket price ${bill}")
    else:
        bill = 15;
        print(f"Adult ticket price ${bill}")
    want_photo = input("Do you want to take photos while riding, if yes then you have to pay $3 more\ny/n: ")
    if want_photo =="Y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("You have no permission to ride on the rollar coaster")