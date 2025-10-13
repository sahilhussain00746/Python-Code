#Range function

print(range(1, 10)) #it don't works with print

for number in range(1, 10): #print upto 9,
    print(number)

print("\n")
for number in range(1, 10, 2): #here it will add 2 every time upto ten
    print(number)
    
#Doing sum using range
total = 0
for number in range(1, 101):
    total += number
    
print(total)