# 1. pop()

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using pop() to remove key 'b'
value = my_dict.pop('b')
print(value)       # Output: 2
print(my_dict)    # Output: {'a': 1, 'c': 3}

# 2. popitem()

my_dict = {'a': 1, 'b': 2, 'c': 3}

key_value = my_dict.popitem()
print(key_value)  # Output: ('c', 3)
print(my_dict)    # Output: {'a': 1, 'b': 2}

# 3. setdefault()

my_dict = {'a': 1, 'b': 2}
value_c = my_dict.setdefault('c', 3)
print(value_c)    # Output: 3 (newly added)
print(my_dict)    # Output: {'a': 1, 'b': 2, 'c': 3}
