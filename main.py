# # variables = A container for a value (string, integer, float, boolean)
# # A variable behaves as if it was the value it contains
#
# name = "Vincent"
# age = 22
# number = [1,2,3,4,5,6,7,8,9]
# pi = 3.14159265359
# print(name)
# print(age)
# print(number)
# print(pi)
#
# # naming variables when naming variables use either camel casing or lower case for example fullName or full_name do not start a variable with a capital letter
# name = "Vincent"
# full_name = "Vincent Mugondora"
# print(name)
# print(full_name)
#
# # data types
# brand = "vincent code"
# age = 22
# pi = 3.14159265359
# isAdult = False
# number = [1,2,3,4,5,6,7,8,9]
# print(type(brand))
# print(type(age))
# print(type(number))
# print(type(pi))
# print(type(isAdult))
#
# if isAdult:
#     print("You are an adult")
# else:
#     print("You are not an adult")
#
#
# # Typecasting = the process of converting one variable from one data type to another
# # str(), int(), float(), bool()
#
# name = "Vincent"
# age = 25
# gpa = 3.6
# is_Student = True
#
# gpa = int(gpa)
# age = float(age)
# age = str(age)
# name = bool(name)
#
# print(gpa)
# print(name)
# print(type(age))
#
# # input()= A function that prompts the user to enter data
# # Returns the entered data as a string
#
# names = input("Enter your name: ")
# ages = input("Enter your age: ")
#
# ages = int(ages)
# ages = ages + 1
#
# print(f"Hello {names}")
# print(f"You are {ages} years old")

# # exercise 1
# length = input("Enter the length of a rectangle: ")
# width = input("Enter the width of a rectangle: ")
# area = int(length) * int(width)
# print(f"The area of the rectangle is {area}cm")

# # exercise 2 Shopping Cart program
# item = input("Enter the item you want to buy: ")
# quantity = int(input("Enter the quantity of the item you want to buy: "))
# price = float(input("Enter the price of the item you want to buy: "))
# total = price * quantity
#
# print(f"The total price of the item you want to buy is ${total}")

# # Madlibs
# # Word game where you create a story
# # by filling in the blanks
#
# adjective1 = input("Enter adjective: ")
# noun1 = input("Enter noun: ")
# adjective2 = input("Enter adjective: ")
# verb1 = input("Enter verb: ")
# adjective3 = input("Enter adjective: ")
#
# print(f"Today l went to a {adjective1} zoo.")
# print(f"In an exhibit l saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# friends = 6
#
# # friends = friends + 1
# # friends += 1
# # friends -= 1
# # friends = friends * 3
# # friends *= 3
# # friends = friends / 2
# # friends /= 2
# # friends = friends ** 2
# # friends **= 2
# # remainder = friends % 2
#
# # print(remainder)

# x = 3.14
# y = 4
# z = 5
#
# # rounded_x = round(x)
# # result = abs(y)
# # result = pow(4,3)
# # result = max(x, y, z)
# result = min(x, y, z)
#
# print(result)

import math

# print(math.pi)
# print(math.e)
# print(math.sqrt(9))
# print(math.ceil(9.9))
# print(math.floor(9.9))

import math

# # Get radius input from user
# radius = input("Enter the radius of a circle: ")
#
# # Calculate circumference
# circumference = 2 * math.pi * float(radius)
#
# # Use ceil or floor based on the decimal part of circumference
# decimal_part = circumference % 1  # Get the decimal part
# if decimal_part < 0.5:
#     rounded_circumference = math.floor(circumference)  # Use floor if remainder < 0.5
# else:
#     rounded_circumference = math.ceil(circumference)   # Use ceil if remainder >= 0.5
#
# print(f"The rounded circumference is: {rounded_circumference}")
