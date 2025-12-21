#What is dictionary and how it works

programming_dictionary = {
    "Bug": "A bug is an error or mistake in a program that causes it to work incorrectly or crash.",
    "Loop": "A loop is used to repeat a block of code multiple times until a condition is met.",
    "Function":"A function is a block of reusable code that performs a specific task.",
    123 : "A 123 is used to repeat a block of code multiple times until a condition is met.",
} #this is a dictionary

print(programming_dictionary["Loop"]) #you can print like this

programming_dictionary["Sahil"] = "Hello sahil hussain" # like this you can add a new key

print(programming_dictionary) #this will print the complete dictionary

programming_dictionary = {} #Like this you can make the dictionary empty

#How to print using loop
for key in programming_dictionary:
    print(key) #This will only print the key
    print(programming_dictionary[key]) #This will print the statement
