"""
    In this example, We are going to leverage String operations
"""

# Create a basic String and print index for a single character
# Note: it returns index for first occurrence, for example if there are two 'i i' present,
# and you are looking for index number for 'i' it will return index for first occurrence
simpleString = "Hi, I am simple String"

# Print the index number of 'i' from above String
print("The i contains at index %d " % simpleString.index('i'))


# Python String count method example
# This method return occurrence of a given string from another string
# For example, string "hi this is..." so if you pass count('i'), it should return 3
# Because the 'i' present in this String for 3 times
simpleString = "Hi, this is Nurujjaman Pollob"

# Print occurrence of 'i' in the simpleString
print("The i is present in this string for %d times" % simpleString.count('i'))

# Print a slice/range of string example
# The ending index is exclusive
print("The slice of string from index 0 to index 5(exclusive) are -> %s" % simpleString[0:5])

# Reverse a string
print("This string -> '%s' is reversed to -> '%s'" % (simpleString, simpleString[::-1]))

# Convert to uppercase and lowercase
print("This string uppercase to -> %s" % simpleString.upper())
print("This string lowercase to -> %s" % simpleString.lower())

# String startswith example
# this method checks that if a given phrase is contains in another
# string and is start with that
print("This string is starts with Hi -> %s" % simpleString.startswith("Hi"))
