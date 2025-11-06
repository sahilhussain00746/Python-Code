def greeting():
    print("Hello Sahil")
    print("How are You\n")
    
greeting()

def greeting_with_name(name): #Here we are receiving the parameter
    print(f"Hello {name}")
    print(f"Well done {name}")
    
greeting_with_name("Sahil") #Here we are passing the argument
greeting_with_name("hussain")