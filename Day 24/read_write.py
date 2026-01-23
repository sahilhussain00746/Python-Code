# file = open("G:/AI/Python/Code/Day 24/my_file.txt")
# contents = file.read()
# print(contents) 
# file.close() # In this method you have to close the file

# with open("G:/AI/Python/Code/Day 24/my_file.txt") as file:
#     content = file.read()
#     print(content)
    
#Write to the file
# with open("G:/AI/Python/Code/Day 24/my_file.txt", mode="a") as file:
#     file.write("\nI am write code")
#     #in the mode we can write r=read, w=write, a=append

#If There is not file exit then it create it by own
with open("new_file.txt", mode="a") as file:
    file.write("New file")