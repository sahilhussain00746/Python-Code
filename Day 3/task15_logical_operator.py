"""or is used when we need to choose one from two,
means any one is true then the answer is true"""

"""and is used when we need to choose both from two or more
means both need to true for the answer true"""

"""not is use for say no"""

a = 10
if a>8 or a<12: #there is will only check once if it get 1 at first check
    print("This is or")
else:
    print("This is not or")
    
if a > 8 and a > 12: #Here it will check both when is alread get 1 at first
    print("This is and")
else:
    print("This is not and")
    
if not a == 10:
    print("This is false")
elif not a!= 10:
    print("This is true")