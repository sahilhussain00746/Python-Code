#Question file BMI (Body mass index)
height = 1.65
weight = 84

height = height ** 2 #this is doing power 2
bmi = weight/height
print("Hence the bmi is " + str(bmi)) #It is print the flaot which very large number after decimal point
print(round(bmi)) #now it will print the round up value

#if you want to roundup upto some digit after decimal point then
print(round(bmi, 2)) #now it will print two digit after decimal point