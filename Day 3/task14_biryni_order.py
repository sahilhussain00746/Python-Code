print("Welcome to Biryani hub")
size = input("Enter plate type.\nHalf(H)\nSingle(S)\nFull(F)\n")
salad = input("Do you need extra salad Y/N\n")
rayta = input("Do yo need extra rayta Y/N\n")
bill = 0

#for half plate biryani
if size == "H":
    bill += 80
    
#for single plate biryani
elif size == "S":
    bill += 150
    
#for full plate biryani
elif size == "F":
    bill += 250
    
if salad == "Y":
    bill += 10
    
if rayta =="Y":
    bill += 10  
          
print(f"Your total bill is: {bill}")