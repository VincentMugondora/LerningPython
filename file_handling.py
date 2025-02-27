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
f.write("Neil")
f.close()
