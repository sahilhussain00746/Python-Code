import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

cal_book = { #Creating a dictionary
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculation():
    print(art.logo)
    f_input = float(input("Enter Your first number: ")) 
    should_continue = True
    while should_continue:
        
        for letter in cal_book:
            print(letter)
            
        operator = input("Choose Your operation: ")
        s_input = float(input("Enter Your second number: "))
        answer = cal_book[operator](f_input, s_input)
        print(f"Output {f_input} {operator} {s_input } : {answer}")
        
        will_continue = input(f"Type 'y' for continue adding in {answer} or Type 'n' for restart the calculation: ").lower()
        
        if will_continue == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculation()
        
    
    
calculation()
"""operation = cal_book["*"] # WE can do this also 
print(operation(3, 6))""" # cal_book[operator](f_input, s_input)