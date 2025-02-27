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
def reverse_string(string):
    return string[::-1]
        

print(reverse_string("Hello"))

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

