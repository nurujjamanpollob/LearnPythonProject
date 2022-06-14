# Define a simple addition operator
simpleAddition = 2 + 2

# Print
print(" 2 add 2 equals %s " % simpleAddition)

# Do subtraction
simpleSubtraction = 4 - 2

# Print
print(" 4 subtract 2 equals %s " % simpleSubtraction)

# Simple multiplication
simpleMultiplication = 4 * 3

# Print
print(" 4 multiplication 3 equals %s " % simpleMultiplication)

# Simple division
simpleDivisionReturnFloat = 4 / 2  # returns float, ref https://docs.python.org/3/tutorial/introduction.html
# and look for Division reference

# Print
print(" 4 divide 2 equals %s is resulting in float" % simpleDivisionReturnFloat)

"""
    If you use // to divide numbers, you can get a Integer result, instead of Float
    Reference https://docs.python.org/3/tutorial/introduction.html
"""
simpleDivisionReturnInteger = 4 // 2  # Reruns float

# Print
print(" 4 divide 2 equals %s resulting in Integer" % simpleDivisionReturnInteger)

# Simple Modulus/Remainder
simpleMod = 26 % 8  # Should return 2

# Print
print(" 26 mod 8 should left remainder of %s " % simpleMod)
