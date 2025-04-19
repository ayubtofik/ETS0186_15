# 1. isatty()
import sys

# Check if standard input is a terminal
if sys.stdin.isatty():
    print("Standard input is a terminal.")
else:
    print("Standard input is not a terminal.")

# 2. read()

# Open a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()  # Read the entire file
    print(content)

# 3. readeable()
# Open a file in read mode
with open('example.txt', 'r') as file:
    if file.readable():
        print("The file is readable.")
    else:
        print("The file is not readable.")

# Open a file in write mode
with open('example.txt', 'w') as file:
    if file.readable():
        print("The file is readable.")
    else:
        print("The file is not readable.")
