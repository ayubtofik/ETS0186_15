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