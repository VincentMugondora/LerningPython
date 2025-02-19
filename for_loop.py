# For loops in Python:

# 1. Iterating over a range
for i in range(5):
    print(i)

# 2. Iterating over a string
for char in "Hello":
    print(char)

# 3. Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 4. Iterating with enumerate
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

# 5. Using a step in range
for i in range(0, 10, 2):
    print(i)

# 6. Nested for loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# 7. Using break and continue
for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(10):
    if num % 2 == 0:
        continue
    print(num)