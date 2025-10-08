#list
# list_name = [item1, item2] Structuer of list
fruit = ["apple", "banana", "orange", "lemon", "Watermelon"]

print(fruit[0]) #like this we can print the item of any list
print(fruit[1])

#we can also retrive the item using negative numbers like -1, -2
print(fruit[-1])

#we can change the values also
fruit[2] = "mango" #now at index two mango relpace orange
print(fruit[2])

fruit.append("Sahil") #this append use to add a item at last 

#we can also add another list in this using exten
fruit.extend(["hello", "hii", "how"])

print(fruit) #This will print the whole list at a time