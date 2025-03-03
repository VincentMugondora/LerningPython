import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())


for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("File not found")
finally:
    f.close()


# Append - creates a new file if doesn't exist

f = open("names_list.txt", "a")
f.write("Vincent\n")
f.close()

f = open("names_list.txt",)
print(f.read())
f.close()

# Write (overwrite)
f =open("context.txt", "w")
f.write("l deleted all of the context\n")
f.close()

f = open("context.txt",)
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()


# creates a file but throws an error if it already exists
if not os.path.exists("viny.txt"):
    f = open("viny.txt", "x")
    f.close()

# Delete a file

# Avoid an error if it doesn't exist
if os.path.exists("viny.txt"):
    os.remove("viny.txt")   
else:
    print("File does not exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names_list.txt", "w") as f:
    f.write(content)