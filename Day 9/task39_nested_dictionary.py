capital = {
    "Bihar" : "Patna",
    "Telangana" : "Hyderabad", 
} #This is a simple dictionary

#The nested list
nest_list = ["Sahil", "hussain", ["Hello", "World"]]
print(nest_list[2][0]) #Like this we can access the element in the nested list

#The nested dictionary
nested_city = {
    "Bihar" : ["Samastipur", "Dharbhanga", "Muzaffarpur"],
    "Telangana" : ["Rangareddy", "Gachibowali", "Hyderabad"]
} #This is a nested loop
print(nested_city["Bihar"][0])

travelling = {
    "Bihar" : {
        "visited_count" : 5,
        "Name" : ["Sahi", "Hussain"]
    }, 
    "Telangana" : {
        "cities" : ["Rangareddy", "Gachibowali", "Hyderabad"],
        "Name " : ["Nabeel", "Nasir"]
    }
}

print(travelling["Bihar"]["Name"][0]) #Like this you can access the items in nested in the list
