#Global Scope
enemies = 1 

def increase_enemine():
    enemies = 2 #This variable is different from previous 
    print(enemies) #2

increase_enemine()
print(enemies) #1

def watering():
    water_plant = 1
    print(water_plant)
    
#print(water_plant) #i thing shows an error because water_plant is local scope

#To access the global variable when have to tell the compiler
mountain = 3

def print_mount():
    global mountain #here we are accessing the global variable
    print(mountain)