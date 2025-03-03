# Convert Decimal to Binary
# Write a function that converts a decimal number (less than 1024) into its binary equivalent1.

# def decimal_to_binary(decimal):
#     return bin(decimal)[2:]  


# decimal_num = 1024
# binary_num = decimal_to_binary(decimal_num)
# print(binary_num)

# Count Vowels in a String
# Create a function that counts the vowels (a, e, i, o, u) in a given word

# def count_vowels(word):
#     vowels = ["a", "e", "i", "o", "u"]
#     count = 0
#     for char in word:
#         if char in vowels:
#             count += 1
#     return count


# word = "vinegar"
# vowel_count = count_vowels(word)
# print(vowel_count)


# Hide Credit Card Number
# Write a function that masks all but the last four digits of a credit card number with asterisks1.

# def hide_credit_card_number(credit_card_number):
#     return f"XXXX-XXXX-XXXX-{credit_card_number[-4:]}"


# credit_card_number = "1234567890123456"
# masked_credit_card = hide_credit_card_number(credit_card_number)
# print(masked_credit_card)

# def calculator(a, b, operator):
#     while True:
#         if operator == "+":
#             return a + b
#         elif operator == "-":
#             return a - b
#         elif operator == "*":
#             return a * b
#         elif operator == "/":
#             return a / b
#         else:
#             return "Invalid operator"
        


# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# operator = input("Input operator: ")
# result = calculator(a, b, operator)
# print(result)

# def palindrome_checker(word):
#     new_word = word
#     if new_word == word[::-1]:
#         return f"{word[::-1]} is a palindrome"
#     else:
#         return f"{word[::-1]} is not a palindrome"

# word = input("Enter a word: ")

# result = palindrome_checker(word)

# print(result)

# def find_extra_char(str1, str2):
#     str1 = set(str1)
#     str2 = set(str2)
    
#     if str1 != str2:
#         extra_char = str1.symmetric_difference(str2)
#         return f"Extra character found: {extra_char}"
#         return "No extra character found"
#     else:
#         return f"No extra character found" 


# str1 = "abcdf"
# str2 = "abcdeg"

# print(find_extra_char(str1, str2))

# name = "Hello World!"

# print(name[5:-1:], name[0:5:])

# def reverse_words(input_string):
#     # Split the string into a list of words
#     words = input_string.split()
    
#     # Reverse the list of words
#     reversed_words = words[::-1]
    
#     # Join the reversed list back into a string
#     reversed_string = " ".join(reversed_words)
    
#     return reversed_string

# # Example usage
# input_string = "Vincent Mugondora"
# print("Reversed string:", reverse_words(input_string))  # Output: "World Hello"


# Friday the 13th Detector
# Create a function that checks if a given month and year contain a Friday the 13th

# def is_friday_the_13th(month, year):
#     import calendar
    
#     # Get the number of days in the given month and year
#     num_days = calendar.monthrange(year, month)[1]
    
#     # Iterate through each day of the month
#     for day in range(1, num_days + 1):
#         # Get the day of the week for the current day
#         day_of_week = calendar.weekday(year, month, day)
        
#         # Check if the day of the week is Friday and if it's the 13th
#         if day_of_week == 4 and day == 13:
#             return True
    
#     return False

# # Example usage
# month = 4
# year = 2020
# print(is_friday_the_13th(month, year))  # Output: True

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

def odd_even_positions(l1, l2):
    for index in l1 and l2:
        if index % 2 == 0:
            return l1[index] and l2[index]


print(odd_even_positions(l1, l2))  # Output: [4, 6, 12, 16, 20, 18, 28]      