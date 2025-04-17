# 1. issubset()
setA = {1, 2}
setB = {1, 2, 3, 4}

print(setA.issubset(setB))  # Output: True

# 2. issuperset()
setA = {1, 2, 3, 4}
setB = {1, 2}

print(setA.issuperset(setB))  # Output: True

# 3. update()
setA = {1, 2}
setB = {2, 3, 4}

setA.update(setB)
print(setA)  # Output: {1, 2, 3, 4}
