#if we find the length of a number like we can't directly we need to change it in string
# len(1234) #it will give a type error

len("Hello")

#Check the data type
print(type("Hello"))
print(type(123))
print(type(23.4))

# int()
# float()
# str()
# bool()

#Type conversion
# int(123) like this you can change
print("123" + "456") #this will concatanate
print(int("123") + int("456")) #this will add the values

#pause question
print("Numers of letter in your code: " + str(len(input("Enter your name: "))) )
