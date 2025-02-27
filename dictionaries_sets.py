# Dictionaries
# A dictionary is a collection of key-value pairs. It is an unordered collection of items, where each key is a dictionary containing a key-value pair.

# Creating a dictionary
# You can create a dictionary by placing a comma-separated sequence of key-value pairs within braces { }, with a colon : separating the key and the value.
# Example: my_dict = {"key1": "value1", "key2": "value

my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict2 = {"name": "John", "age": 30, "city": "New York"}


# Accessing values in a dictionary
# You can access the value of a key in a dictionary by using the key as an index.

print(my_dict["name"])
print(my_dict.get("age"))

# list all keys
print(my_dict.keys())

# list all values
print(my_dict.values())

# list all key/value pairs as tuples
print(my_dict.items())

# verify a key exists in the dictionary
print("name" in my_dict)
print("surname" in my_dict)

# change values in a dictionary
my_dict["age"] = 31
my_dict.update({"city": "San Francisco"})
print(my_dict)

# delete a key/value pair from a dictionary
print(my_dict.pop("age"))
print(my_dict)

# adding items in a dictionary
my_dict["bank"] = "NedBank"
print(my_dict)

print(my_dict.popitem())  # tuple
print(my_dict)

# delete and clear the dictionary
my_dict["bank"] = "NedBank"
del my_dict["name"]
print(my_dict)

my_dict2.clear()
print(my_dict2)

del my_dict2

# copy dictionaries
# my_dict2 = my_dict # this is a reference
# print("Bad Copy")
# print (my_dict2)
# print(my_dict)

# my_dict2["name"] = "Jane"
# print(my_dict)

my_dict2 = my_dict.copy()
print("Good Copy!")
my_dict2["name"] = "Jane"
print(my_dict)
print(my_dict2)

# or use the dict() constructor function
my_dict3 = dict(my_dict)
print("Good Copy!")
print(my_dict3)

# Nested dictionaries
member1 = {
    "name": "John",
    "age": 30
}
member2 = {
    "name": "Jane",
    "age": 18
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets
# A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).

nums = {1, 2, 3, 4} 

print("THESE ARE SETS")

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))

# No duplicates allowed
nums = {1, 2, 3, 1, 2}
print(nums)

# True is a dupe of 1 and False is a dupe of 0
nums = {1, 2, 3, True, False,4,0}
print(nums)

# Check if a value is in a set
print(2 in nums)
# you cant refer to an element in the set with an index position or a key
# you can only check if a value is in the set with the 'in' keyword

# Add an element to a set
nums.add(5)
print(nums)

# Add elements from one set to another
morenums = {6, 7, 8}
nums.update(morenums)
print(nums) # you can use update with lists, tuples and dictionaries too

# Merge two sets to create a new set
one = {1, 2, 3}
two = {2, 3, 4, 5}

my_new_set = one.union(two)
print(my_new_set)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4, 5}

my_new_set = one.intersection(two)
print(my_new_set)

# Keep only the unique elements
one = {1, 2, 3}
two = {2, 3, 4, 5}

my_new_set = one.symmetric_difference(two)

print(my_new_set)
