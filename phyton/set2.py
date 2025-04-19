# 1. difference():

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
result = set1.difference(set2)  # result is {1, 2}

# 2. difference_update():
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.difference_update(set2)  # set1 is now {1, 2}

# 3. tell():
# Create and write to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!")

# Open the file in read mode
with open('example.txt', 'r') as file:
    # Read the first 5 characters
    content = file.read(5)
    print("Content read:", content)

    # Get the current position in the file
    position = file.tell()
    print("Current position in the file:", position) #output Content read: Hello # output Current position in the file: 5




     


     

     

     
