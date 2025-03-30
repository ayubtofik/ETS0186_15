# 1. str.isspace()

text1 = "   "
text2 = "Hello"

print(text1.isspace())  # Output: True
print(text2.isspace())  # Output: False

# 2. str.format()

name = "Alice"
age = 30

formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

# 3. f-strings

name = "abebe"
age = 25

formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is abebe and I am 25 years old.

# 4. len()

text = "Hello, World!"

length_of_text = len(text)
print(length_of_text)  # Output: 13

