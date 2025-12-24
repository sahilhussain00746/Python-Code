#There is no block scope in python like c++ and java
number = 10
enemies = ["Skeleton", "Alien"]

if number == 5:
    new_enemy = enemies[0]
    
print(new_enemy) #We can access this because of no block scope in python

def game():
    #best practice to write the variable before use in the conditional
    old_enemy = "" #this is the variable
    if number > 5:
        old_enemy = enemies[0]
    
    print(old_enemy) #this is showing some mistake because of not defined
    
game()
