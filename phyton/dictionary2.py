# 1. get()
my_dict = {'name': 'Abebe', 'age': 30, 'city': 'bole'}

name = my_dict.get('name')
print(name)  # Output: abebe

country = my_dict.get('country', 'USA')
print(country)  # Output: USA

# 2. items()

for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output:
# name: abebe
# age: 30
# city: bole

# 3. keys()
my_dict = {'name': 'abebe', 'age': 30, 'city': 'bole'}

for key in my_dict.keys():
    print(key)

# Output:
# name
# age
# city
