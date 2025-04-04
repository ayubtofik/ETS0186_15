# 1. insert()

fruits = ['apple', 'banana', 'cherry']

# Insert 'orange' 
fruits.insert(1, 'orange')

print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

# 2. pop() 

numbers = [1, 2, 3, 4, 5]

# Pop the last element
last_number = numbers.pop()

print(last_number)  # Output: 5
print(numbers)      # Output: [1, 2, 3, 4]

# 3. remove()

colors = ['red', 'blue', 'green', 'blue']

colors.remove('blue')

print(colors)  # Output: ['red', 'green', 'blue']
