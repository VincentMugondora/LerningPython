# # functions

# def greet_message():
#     print("Hi there!")
#     print("How are you today?")


# greet_message()

# # Arguments

# def add_numbers(num1, num2):
#     return num1 + num2


# result = add_numbers(5, 10)

# print(result)


# # We Have functions that:
#     # 1. Perform a task
#     # 2. Return a value

# def get_greeting(name):
#     return f"Hello {name}"

# try:
#     message = get_greeting("John")
#     with open("content.txt", "w") as file:
#         file.write(message)
#     print(message)
# except Exception as e:
#     print(f"An error occurred: {e}")

# def increment (number, by=1):
#     return number + by  


# print (increment(2, 4))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2,3,4,5))

# def save_user(**user):
#     print(user)


# save_user(id=1, name="John", age=22)

# # Scope
# message = "a"

# def greet():
#     message = "b"   
#     print(message)


# greet()

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(45))