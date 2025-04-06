# 1. clear()

my_dictionary = {'a': 1, 'b': 2, 'c': 3}

# Clearing the dictionary
my_dictionary.clear()

print("Dictionary after clear():", my_dictionary) # output: Dictionary after clear(): {}

# 2. copy()

original_dict = {'x': 10, 'y': 20}

# Creating a copy of the original dictionary
copied_dict = original_dict.copy()

# Modifying the copied dictionary
copied_dict['x'] = 30

print("Modified Copied Dictionary:", copied_dict) # output: {'x': 30, 'y': 20}
print("Original Dictionary after modifying copy:", original_dict) # output: {'x': 10, 'y': 20}

# 3. fromkeys()

keys = ['name', 'age', 'city']
default_value = 'unknown'

new_dict = dict.fromkeys(keys, default_value)

print("New Dictionary created using fromkeys():", new_dict)
# output: New Dictionary created using fromkeys(): {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}


