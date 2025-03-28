
# 1. str.strip()

text = "***Hello, World!***"
cleaned_text = text.strip('*')
print(cleaned_text)  # Output: "Hello, World!"

2. #str.lstrip()

text = "   Hello, World!   "
left_cleaned_text = text.lstrip()
print(left_cleaned_text)  # Output: "Hello, World!   "

# Removing specific characters
text = "***Hello, World!"
left_cleaned_text = text.lstrip('*')
print(left_cleaned_text)  # Output: "Hello, World!"

# 3. str.rstrip()

text = "Hello, World!***"
right_cleaned_text = text.rstrip('*')
print(right_cleaned_text)  # Output: "Hello, World!"

#4. str.split()

text = "Hello, World! How are you?"
words = text.split()
print(words)  # Output: ['Hello,', 'World!', 'How', 'are', 'you?']
