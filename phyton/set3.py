# 1. intersection()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)  # Output: {3, 4}

# 2. intersection_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)  # Output: {3, 4}

# 3. isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True

