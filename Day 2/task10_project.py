# A bill calculator
print("Welcome to the bill calculator")
bill = float(input("What is the total bill: "))
tip = float(input("How much tip you want to give: "))
person = float(input("In how many people the bill will divide: "))
total = (bill + bill*tip/100)/person

print(f"Each one have to pay {round(total,2)}")
