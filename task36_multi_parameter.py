#Passing the multiple parameters here
def greeting_with(name, location):
    print(f"Hello {name}")
    print(f"I am form {location}")
    
greeting_with("Sahil", "Bihar") #here sequence matters

#keyword arguments (here sequence don't matters)
greeting_with(name="Hussain", location="India")
greeting_with(location="India", name="Hussain")