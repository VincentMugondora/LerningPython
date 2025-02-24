# # The `collections` module in Python provides alternatives to Python's general-purpose built-in containers like dict, list, set, and tuple. Here are the main types provided by the `collections` module:

# # 1. **Counter**: A `Counter` is a dictionary subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
#     ```python
#     from collections import Counter
#     counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
#     print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
#     ```

# 2. **defaultdict**: A `defaultdict` is a dictionary subclass that calls a factory function to supply missing values. It is useful when you want to initialize the dictionary with default values.
#     ```python
#     from collections import defaultdict
#     default_dict = defaultdict(int)
#     default_dict['apple'] += 1
#     print(default_dict)  # Output: defaultdict(<class 'int'>, {'apple': 1})
#     ```

# 3. **deque**: A `deque` (double-ended queue) is a list-like container with fast appends and pops on either end. It can be used to implement queues and stacks.
#     ```python
#     from collections import deque
#     d = deque([1, 2, 3])
#     d.append(4)
#     d.appendleft(0)
#     print(d)  # Output: deque([0, 1, 2, 3, 4])
#     ```

# 4. **namedtuple**: A `namedtuple` is a factory function for creating tuple subclasses with named fields. It is useful for creating simple classes to group together a few related values.
#     ```python
#     from collections import namedtuple
#     Point = namedtuple('Point', ['x', 'y'])
#     p = Point(1, 2)
#     print(p)  # Output: Point(x=1, y=2)
#     ```

# 5. **OrderedDict**: An `OrderedDict` is a dictionary subclass that remembers the order in which its contents are added. It is useful when the order of items is important.
#     ```python
#     from collections import OrderedDict
#     ordered_dict = OrderedDict()
#     ordered_dict['banana'] = 3
#     ordered_dict['apple'] = 4
#     ordered_dict['pear'] = 1
#     print(ordered_dict)  # Output: OrderedDict([('banana', 3), ('apple', 4), ('pear', 1)])
#     ```

# These specialized container datatypes provide additional functionality and can be very useful in various scenarios.

# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {}  unordered and immutable but Add/Remove OK. No duplicates
# Tuple = () ordered and immutable. Duplicates OK. FASTER

fruits = ["apple", "banana", "cherry", "orange"]

# print(fruits[0])

for fruit in fruits:
    if fruit == "apple" or fruit == "banana":
        print(f"The {fruit} is delicious")