# Dictionaries
# A dictionary is a collection of key-value pairs. It is an unordered collection of items, where each key is a dictionary containing a key-value pair.

# Creating a dictionary
# You can create a dictionary by placing a comma-separated sequence of key-value pairs within braces { }, with a colon : separating the key and the value.
# Example: my_dict = {"key1": "value1", "key2": "value

my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing values in a dictionary
# You can access the value of a key in a dictionary by using the key as an index.

name = my_dict["name"]
age = my_dict["age"]
city = my_dict["city"]

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

# Updating values in a dictionary   