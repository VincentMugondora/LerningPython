# fruits = ("banana", "orange", "pineapple", "mango")

# # print(fruits[2])

# # numbers = (5, 10, 15, 20, 25, 30)

# # print(numbers[2:5])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # numbers[0] = 10
# # print(numbers)

# # my_list = list(fruits)

# # my_list.append("guava")

# # my_tuple = tuple(my_list)

# # print(my_tuple)

# # set1 = {1,2,3,4,}
# # set2 = {3,4,5,6}

# # print(set1.union(set2))
# # print(set1.intersection(set2))

# # control flow

# # for x in range(1, 11):
# #     print(x)

# num = 5

# while num <= 5 and num >= 0:
#     print(num)
#     num -= 1


# functions

# def add_numbers(a, b):
#     return a + b


# print(add_numbers(5, 10))


# even or odd

# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# print(check_even_odd(5))


# Prime Number

# for n in range (2, 10):
#     for x in range (2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n/x}")
#             break
#     else:
#         print(f"{n} is a prime number")


# def initlog(*args):
#     pass


# for x in range(0, 20):
#     if x % 2 == 0:
#         print(x)


# for i in range (2, 21, 2):
#     print(i)


# names = ["John", "Jane", "Doe", "Mary", "Peter"]

# for name in names:
#     print(f"Hello {name}")

# for x in range(2, 21):
#     for i in range(2, x):
#         if x % i == 0:
#             print(f"{x} equals {i} * {x/i}")
            

# Reverse a string
# def reverse_string(string):
#     return string[::-1]
        

# print(reverse_string("Hello"))

# Find the Maximum in a List

# def find_max(list):
#     maxEE = list[0]
#     for num in list:
#         if num > maxEE:
#             maxEE = num
#     return maxEE


# numbers = [35, 10, 15, 20, 25, 30]
# print(find_max(numbers))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return f"{n} is not a prime number"
#     return f"{n} is a prime number"
    

# print(is_prime(6))

# pi = 3.14159 # approximate
# diameter = 3

# # Create a variable called 'radius' equal to half the diameter
# radius = diameter/2

# # Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
# area = pi * radius**2
# # Check your answer
# print(area)

# print(2**2)

# Variables representing the number of candies collected by alice, bob, and carol
# alice_candies = 121
# bob_candies = 77
# carol_candies = 109

# # Your code goes here! Replace the right-hand side of this assignment with an expression
# # involving alice_candies, bob_candies, and carol_candies
# to_smash = (121 + 77 + 109) - (round((121 + 77 + 109) / 3) * 3 ) 
# print(to_smash)

# return least differrence
# def least_diff (a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)


# print(least_diff(23, 50, 42))


# # What would happen if we didn't include the return keyword in our function?

# def least_difference(a, b, c):
#     """Return the smallest difference between any two numbers
#     among a, b and c.
#     """
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)
    
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7),
# )

# def mult_by_five(x):
#     return 5 * x

# def call(fn, arg):
#     """Call fn on arg"""
#     return fn(arg)

# def squared_call(fn, arg):
#     """Call fn on the result of calling fn on arg"""
#     return fn(fn(arg))

# print(
#     call(mult_by_five, 1),
#     squared_call(mult_by_five, 1), 
#     sep='\n', # '\n' is the newline character - it starts a new line
# )

# full_name = "vincent mugondora"
# print(full_name[::-1])

# name = "Jennifer"
# print(name[1:-1])

# secret_num = 9
# guess_counter = 0 
# guess_limit = 3
# while guess_counter < guess_limit:
#     guess = int(input("Guess: "))
#     guess_counter += 1
#     if guess == secret_num:
#         print(f"You guessed correctly.\n")
#         break
# else:
#     print("You guessed incorrectly")

# command = ""
# started = False

# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car started")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "help":
#         print(""" 
# stop - to stop the car
# quit - to quit the game
# start - to start the car
#         """)
#     elif command == "quit":
#         break
#     else:  
#         print("Sorry l don't this understand command")


# for item in [2, 3, 4, 5, 6, 7]:
#     item = item*10 
#     print(item)

# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(total)


# for x in range (4):
#     for y in range (3):
#         print(f"{x}, {y}")

# numbers = [2, 2, 2, 2, 10]

# for number in numbers:
#     output = ""
#     for count in range(number):
#         output += "X"
#     print(output)

# command = ""
# started = False

# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("The car is already started")
#         else:
#             started = True
#             print("Started the car")
#     elif command == "stop":
#         if not started:
#             print("The car is already stopped")
#         else:
#             started = False
#             print("Stopped the car")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit the game
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("l do not understand the command")


# numbers = [5, 2, 5, 35, 2, 2]

# def order(numbers):
#     # Sort the list in descending order
#     sorted_numbers = sorted(numbers, reverse=True)
    
#     # Print each number
#     for number in sorted_numbers:
#         print(number)

# # Example usage
# numbers = [5, 2, 9, 1, 7, 3]
# order(numbers)

# def order(numbers):
#     # Make a copy of the list to avoid modifying the original list
#     numbers_copy = numbers.copy()
    
#     while numbers_copy:
#         # Find the maximum number in the current list
#         max_number = max(numbers_copy)
        
#         # Print the maximum number
#         print(max_number)
        
#         # Remove the maximum number from the list
#         numbers_copy.remove(max_number)

# # Example usage
# numbers = [5, 2, 9, 1, 7, 3]
# order(numbers)


# def numbers(numbers):
#     numbers_copy = numbers.copy()
    
#     while numbers_copy:
#         max_number = max(numbers_copy)
#         print(max_number)
#         numbers_copy.remove(max_number)


# numbers([5, 2, 9, 1, 7, 3])


# 2D LISTS
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)