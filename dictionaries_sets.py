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

# Updating values in a dictionary  
