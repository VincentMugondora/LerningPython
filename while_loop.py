# while Loop
# In Python, we use a while loop to repeat a block of code until a certain condition is met. For example,

# number = 1
#
# while number <= 15:
#     print(number)
#     number = number + 1
#

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello, {name}")

# age = int(input("Enter your age: "))
#
# while age < 0 :
#     print("age can't be negative")
#     age = int(input("Enter your age: "))
#
# print(f"You are {age} years old")

# food = input("Enter food you like (press q to quit): ")
#
# while food != "q":
#     print("It's a " + food)
#     food = input("Enter another food you like: ")
#
# print("Thank you!")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is: {num}")
