# Ceasar Ciper
import art
print(art.logo)

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceasar(original_text, shift_amount, encode_or_decode):
    final_list = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
                
    for letter in original_text:

        if letter not in alphabets:
            final_list += letter
        
        symbol_position = alphabets.index(letter) + shift_amount
        symbol_position %= len(alphabets) #Here it will maintain the balance of the list
        final_list += alphabets[symbol_position]
    print(f"Here is Your {encode_or_decode}d messege: {final_list}")
   
should_continue = True 
while should_continue:

    direction = input("Type Encode to Encrypt and Decode to decrypt: ").lower()
    text = input("Enter your messege: ").lower()
    shift = int(input("Enter shift amount: "))    
    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    
    restart = input("If You wnat to continue press Yes otherwise No: ").lower()
    if restart == "no":
        should_continue = False
        print("Thank You")