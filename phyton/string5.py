# 1. str.join()

words = ['Hello', 'World', 'from', 'Python']
sentence = ' '.join(words)
print(sentence)  # Output: "Hello World from Python"

# 2. str.isalpha()

text1 = "Hello"
text2 = "Hello123"
text3 = ""

print(text1.isalpha())  # Output: True
print(text2.isalpha())  # Output: False
print(text3.isalpha())  # Output: False 

# 3. str.isdigit()

num1 = "12345"
num2 = "123a45"
num3 = ""

print(num1.isdigit())  # Output: True
print(num2.isdigit())  # Output: False
print(num3.isdigit())  # Output: False 

# 4. str.isalnum()

text1 = "Hello123"
text2 = "Hello 123"  
text3 = "12345"
text4 = ""

print(text1.isalnum())  # Output: True
print(text2.isalnum())  # Output: False (contains space)
print(text3.isalnum())  # Output: True
print(text4.isalnum())  # Output: False (empty string)