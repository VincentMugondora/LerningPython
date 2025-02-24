#nested loop = a loop within another loop (outer, inner)

# This script demonstrates the use of nested loops in Python

# Outer loop
# for i in range(1, 4):
#     print(f"Outer loop iteration {i}")
    
#     # Inner loop
#     for j in range(1, 4):
#         print(f"  Inner loop iteration {j}")
    
# This script demonstrates the use of nested loops in Python

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()