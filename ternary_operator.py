#           print or assign one of two values based on a condition
#           X if condition else Y
from os import access

num = 6
a = 10
b = 7
age = 5
temperature = 34
user_role = "admin"

# print ("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b

# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temperature > 30 else "Cold"
access_level = "Full access" if user_role == "admin" else user_role
print(access_level)