score = [12,34,67,87,32,56,32,89,54,66,90,43]

#this is inbuilt sum function
total_sum = sum(score)
print(f"This is computer sum: {total_sum}")

#this is own built function
total_my = 0
for marks in score:
    total_my +=marks
    
print(f"This is my sum: {total_my}")

#Builtin function for max
computer_max = max(score)
print(f"Computer max: {computer_max}")

#This is mine function
max_marks = 0
for marks in score:
    if max_marks < marks:
        max_marks = marks
    
print(f"Mine max: {max_marks}")