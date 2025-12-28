from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Student Name", ["Sahil ", "Maaz", "Aman"])
table.add_column("Course", ["B.tech", "B.tech", "MLT"])

print(table.align) # Currently this is in the center

# We can change the alignment of the table using align function
table.align = "l" # Now is align to left
# "c" --> center, "l" --> left and "r" --> Right

print(table)