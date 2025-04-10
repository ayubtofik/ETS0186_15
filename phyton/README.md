This repository showcases  Python string manipulation methods:  

# 1.** upper()**
    In Python, you can convert strings to uppercase using the upper() method. This method converts all the characters in a string to uppercase, leaving non-alphabetic characters unchanged. It's simple and effective when you need to standardize text, such as for comparisons or formatting.
    This repository showcases three essential Python string manipulation methods:  

# 2. **str.title()**  
   - Converts the first letter of each word to uppercase and the rest to lowercase.  
   - Example: "hello world" → "Hello World"  

# 3. **str.capitalize()**  
   - Capitalizes only the first character of the string and lowercases the rest.  
   - Example: "pYtHon" → "Python"  

# 4. **str.swapcase()** 
   - Swaps uppercase letters to lowercase and vice versa.  
   - Example: "PyThOn" → "pYtHoN"
# 5. **str.find()**:
   - Returns the lowest index where a specified substring is found.
   - Returns `-1` if the substring is not present.

# 6. **str.index()**:
   - Similar to `find()`, but raises a `ValueError` if the substring is not found.

# 7. **str.startswith()**:
   - Checks if a string starts with a specified prefix. Returns `True` or `False`.

# 8. **str.endswith()**
   -This method returns True if the string ends with the specified suffix, otherwise returns False.

# 9. **str.count()**
    - This method returns the number of occurrences of a substring in the string.

# 10. **str.replace(old, new)**
    - This method returns a copy of the string where all occurrences of the old substring are replaced with the new substring.

# 11. **str.strip()**
   - The strip() method removes any leading and trailing  whitespace characters from a string. It can also - remove specified characters if provided as an argument.
# 12. **str.lstrip()**
   - The lstrip() method removes any leading whitespace characters from the left side of the string. -Similar to strip(), it can also remove specified characters.
# **13. str.rstrip()**
   - The rstrip() method removes any trailing whitespace characters from the right side of the string. Like the other methods, it can also remove specified characters.
# **14. str.split()**
   - The split() method splits a string into a list of substrings based on a specified delimiter. By default, it splits by any whitespace and removes extra whitespace.
# **15. str.join()** 
   - The join() method is used to concatenate a sequence of strings (like a list or tuple) into a single  string, with a specified separator between each element.
# **16. str.isalpha()**
   - The isalpha() method checks if all the characters in a string are alphabetic (letters only). It returns True if the string contains only letters and is not empty; otherwise, it returns False.
# **17. str.isdigit()**
   - The isdigit() method checks if all the characters in a string are digits (0-9). It returns True if the string contains only numeric characters and is not empty; otherwise, it returns False.
# **18. str.isalnum()**
   - The isalnum() method checks if all the characters in a string are alphanumeric (letters and digits). It returns True if the string contains only letters and/or digits and is not empty; otherwise, it returns False.
# **19. str.isspace()**
   - The str.isspace() method checks if all characters in a string are whitespace characters (spaces, tabs, newlines, etc.). It returns True if the string is empty or contains only whitespace characters; otherwise, it returns False.
# **20. str.format()**
   - The str.format() method allows you to format strings by inserting values into placeholders defined by curly braces {}. This method is useful for creating dynamic strings and can handle various data types.
# **21. f-strings **
   - F-strings (formatted string literals) are a way to embed expressions inside string literals, using the syntax f"...". They were introduced in Python 3.6 and provide a more concise and readable way to format strings compared to str.format().
# **22. len()**
   - The len() function returns the number of items (length) in an object. When used with strings, it returns the number of characters in the string, including spaces and punctuation.
# **23. str.encode()**
   - The str.encode() method is used to convert a string into bytes. This is particularly useful when you need to encode a string for storage or transmission, as it allows you to specify the encoding format 
# **24. str.islower()**
   - The str.islower() method checks if all the characters in a string are lowercase. It returns True if all characters are lowercase and there is at least one character; otherwise, it returns False.
# **25. str.isupper()**
   - The str.isupper() method checks if all the characters in a string are uppercase. It returns True if all characters are uppercase and there is at least one character; otherwise, it returns False.

 Below is provided definition of some list methods in Python

# **1. append()**
   - The append() method adds a single element to the end of a list. It modifies the original list in place.
# **2. clear()**
   - The clear() method removes all items from the list, leaving it empty. This method modifies the original list in place.
# **3. copy()**
   - The copy() method returns a shallow copy of the list. A shallow copy means that it creates a new list object but does not create copies of nested objects; instead, it references them.
# **4. count()**
   - The count() method returns the number of times a specified value appears in a list.
# **5. extend()**
   - The extend() method adds the elements of an iterable (like a list, tuple, or set) to the end of the current list.
# **6. index()**
   - The index() method returns the index of the first occurrence of a specified value in a list. If the value is not found, it raises a ValueError.
# **7. insert()**
   - The insert() method is used to insert an element at a specified position in a list.
# **8. pop()**
   - The pop() method removes and returns an element from a specified position in the list. If no index is specified, it removes and returns the last item in the list.
# **9. remove()**
   - The remove() method removes the first occurrence of a specified value from the list. If the value is not found, it raises a ValueError.
# **10. reverse()**
   - The reverse() method reverses the elements of a list in place. This means that the original list is modified and no new list is created.
# **11. sort()**
   - The sort() method sorts the elements of a list in ascending order by default. 
   
Below is provided definition of some dictionary methods in Python

# **1. clear()**
   - The clear() method removes all items from the dictionary, resulting in an empty dictionary. This method modifies the dictionary in place and does not return any value.
# **2. copy()**
   - The copy() method returns a shallow copy of the dictionary. This means it creates a new dictionary object with the same key-value pairs as the original dictionary. Changes made to the copied dictionary do not affect the original dictionary.
# **3. fromkeys()**
   - The fromkeys() method creates a new dictionary from the given sequence of keys, with all values set to a specified value (default is None). This method returns a new dictionary and does not modify the original dictionary.
# **4. get()**
   - The get() method is used to retrieve the value associated with a specified key from a dictionary. If the key does not exist, it returns None or a specified default value.
# **5. The items()**
   - The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs. It allows you to iterate over both keys and values.
# **6. keys()**
   - The keys() method returns a view object that displays a list of all the keys in the dictionary. This method is useful when you need to iterate over the keys.
# **7. pop()**
   - The pop() method removes a specified key from the dictionary and returns its corresponding value. If the key is not found, it raises a KeyError. You can also provide a default value that will be returned if the key does not exist.
# **8. popitem()**
   - The popitem() method removes and returns the last inserted key-value pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.
# **9. setdefault()**
   - The setdefault() method returns the value of a specified key. If the key does not exist, it inserts the key with a specified default value and returns that value.
# ** 10.update()**
   - The update() method is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs.It modifies the dictionary in place and can take another dictionary. 
# **11. values()**
   - The values() method returns a view object that displays a list of all the values in the dictionary.