class user:
    # __init__ --> initialize 
    # self parameter will always be there 
    def __init__(self, user_id, username): # Afer creating this when we will create a new user then, we need to pass the parameters
        user.id = user_id
        user.name = username
        user.followers = 0
        

user_1 = user("001", "Sahil") 

print(user_1.id)
print(user_1.followers)

# user_2 = user()
# user_2.id = "002" # This will show some errors
# user_2.username = "Hussain"