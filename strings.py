# name = input("What is your name?: ")
# phone_number = input('Enter your phone number: ')

# length = len(name)
# result = name.find("v")  # finds the first occurance
# result = name.rfind("n")   # finds the last occurance
# result = name.capitalize() # capitalize first letter of a string
# name = name.upper() # capitalize the whole string
# name =  name.lower() # converts all characters to lower case
# result = name.isdigit() # returns true or false
# result = name.isalpha() # returns true or false if it contains only alphabetical characters
# result = phone_number.count('-') # to count how many characters are in a string
# result = phone_number.replace('-', '') # replaces characters within a string

# print(result)

# print(help(str)) # see all methods you can use

# exercise
# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

# solution 1
# if len(username) > 12:
#     print("Your username is too long")
# elif " " in username:
#     print("Your username must not contain spaces")
# elif any(char.isdigit() for char in username):
#     print("Your username must not contain numbers")
# else:
#     print(""
#           "Hello " + username + "!")

# solution 2
# print(username)
# if len(username) > 12:
#     print("Your username is too long")
# elif not username.find(" ") == -1:
#     print("Your username must not contain a space")
# elif not username.isalpha():
#     print("Your username must contain only letters")
# else:
#     print("Welcome " + username + "!")