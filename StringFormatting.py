"""
    Python String formatting

    Python uses C-style string formatting to create new, formatted strings.
    The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
    together with a format string,
    which contains normal text together with "argument specifiers",
    special symbols like "%s", "%f", "%x" and "%d".

    Here is some basic argument specifier, you should know.

    * %s - String (or any object with a string representation, like numbers)
    * %d - Integers
    * %f - Floating point numbers
    * %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
    * %x/%X - Integers in hex representation (lowercase/uppercase)


"""

# This prints out "Hello, Nurujjaman Pollob!"
name = "Nurujjaman Pollob"

# Print output
print("Hello, %s!" % name)

# To use two or more argument specifiers, use a tuple (parentheses)
# This prints out "Nurujjaman Pollob is 23 years old."
name = "Nurujjaman Pollob"
age = 22

# Print
print("%s is %d years old." % (name, age))

"""
    Any object which is not a string can be formatted using the %s operator as well
    
    In below example, I gonna show how to do it.
"""

# This prints out: list: [1, 2, 3]
mylist = [1, 2, 3]

# Print
print(" list is: %s" % mylist)

