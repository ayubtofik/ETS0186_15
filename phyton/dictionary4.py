# 1. update()

my_dict = {'a': 1, 'b': 2}

my_dict.update({'b': 3, 'c': 4})

print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# 2. values()

my_dict = {'a': 1, 'b': 2, 'c': 3}

values = my_dict.values()

print(values)  # Output: dict_values([1, 2, 3])

# If we modify the dictionary
my_dict['d'] = 4

print(values)  # Output: dict_values([1, 2, 3, 4])



