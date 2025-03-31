# 1. str.encode()

original_string = "Hello, World!"
encoded_string = original_string.encode('utf-8')

print("Encoded String:", encoded_string)      # Output: b'Hello, World!'

# 2. str.islower()

string1 = "hello"
string2 = "Hello"

print(string1.islower())  # Output: True
print(string2.islower())  # Output: False

# 3. str.isupper()

string1 = "HELLO"
string2 = "Hello"

print(string1.isupper())  # Output: True
print(string2.isupper())  # Output: False