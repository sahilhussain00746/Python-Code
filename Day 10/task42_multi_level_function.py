def formate_1(text):
    return text+text

def formate_2(text):
    return text.title()

output = formate_2(formate_1("sahil"))
print(output) # Output --> Sahilsahil