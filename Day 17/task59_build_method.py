class user:
    def __init__(self, user_id, username): 
        user.id = user_id
        user.name = username
        user.followers = 0
        user.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = user("001", "Sahil") 
user_2 = user("002", "Hussain")

user_1.follow(user_2)

print(f"Sahil followers: {user_1.followers} ")
print(f"Sahil  following: {user_1.following} ")

print(f"Hussain  followers: {user_2.followers} ")
print(f"Hussain  following: {user_2.following} ")

