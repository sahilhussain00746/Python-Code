import art, data, random
print(art.logo)
people_list = [
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Selena Gomez",
    "Kylie Jenner",
    "Dwayne Johnson",
    "Ariana Grande",
    "Kim Kardashian",
    "Beyoncé",
    "Taylor Swift",
    "Justin Bieber",
    "Virat Kohli",
    "MrBeast",
    "Nicki Minaj",
    "Neymar Jr",
    "Zendaya",
    "Elon Musk",
    "Bill Gates",
    "Akshay Kumar",
    "Shah Rukh Khan",
    "PewDiePie"
]


def ran_genA():
    """Here Generating the random perosn first"""
    return random.choice(people_list)

def ran_genB():
    """Here Generating the random perosn second"""
    return random.choice(people_list)
    
def show_personA(personA):
    """Fetching the data for person first"""
    person = data.people_data[personA]
    print(f"Compare A: {personA}, a {person['profession']} from {person['country']}.")
    return personA


def show_personB(personB):
    """Fetching the data for person first"""
    person = data.people_data[personB]
    print(f"Against B: {personB}, a {person['profession']} from {person['country']}.")
    return personB

def compare_person(personA, personB):
    """Here We are comparing the followers"""
    if data.people_data[personA]["followers"] > data.people_data[personB]["followers"]:
        return personA
    else:
        return personB

personA = ran_genA()
show_personA(personA)

print(art.vs)
score = 0

should_continue = True
while should_continue:
    personB = ran_genB()
    while personA == personB:
        personB = ran_genB()
        
    show_personB(personB)
    
    choice = input("Who have more followers? 'A' or 'B': ").lower()
     
    final_name = compare_person(personA, personB)
    
    if choice =="a":
        user_choice = personA
    elif choice == "b":
        user_choice = personB
    else:
        print("Invalid Input! Please try again")
        continue
    
    if user_choice == final_name:
        print("✅ Correct anser!")
        score += 1
        print(f"Your Total Score: {score}")
        personA = final_name
        show_personA(personA)
        print(art.vs)
    else:
        print("❌ Wrong answer!")
        print(f"Your Total Score: {score}")
        should_continue = False
        
        
    




