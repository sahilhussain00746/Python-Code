#Here we will learn about the function return keyword

#name = "my Name Is SaHil" #.title()
#print(name.title()) # we can also do like this

def word_formate(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"

formated = word_formate("SAhil", "HUSSain")
print(formated)    

"""Bonous Tip"""
def add(n1, n2):
    return n1 + n2

my_calculation = add #Now this variable will act like a function

print(my_calculation(3, 5)) # This will return 8