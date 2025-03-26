# 1. str.find()
text = "this an examplatory,welcome to this respository  ."

# Find the index of 'welcome'
index = text.find('welcome')
print(index)  #output: 18

# Find a substring that doesn't exist
index = text.find('abebe')
print(index)  

# 2.str.index()
text = "Hello, welcome to Python programming."

# Get the index of 'Python'
index = text.index('Python')
print(index)  # Output: 18

#3.str.startswith()
text = "Hello, welcome to Python programming."


starts = text.startswith('Hello')
print(starts)  # Output: True

# Check with a different prefix
starts = text.startswith('Hi')
print(starts)  # Output: False