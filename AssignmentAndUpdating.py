"""
    This example going to show you how to assign value from one variable to another.
"""

simpleVar = 100  # Simple variable

valueFromAnotherVariable = simpleVar + 100  # get value from simpleVar and add 100
# and assign it to valueFromAnotherVariable

# Print
print("valueFromAnotherVariable should print 200 because it taking value from simpleVar which value is 100 and add "
      "100 with is should print %s" % valueFromAnotherVariable)


"""
    This example gonna merge a number with String and assign in new variable
"""

simpleNumber = int(7000)  # Explicit type declaration

# Append number at %s(means as string) with % operator
# Define type as string
simpleString = str("Hi, I am a String, taking a integer from simpleNumber and append it here: %s" % simpleNumber)  #

# Print
print(simpleString)

"""
    Now, I gonna manipulate simpleString and convert simpleNumber to String with str(object) method and assign to 
    simpleString, and clear it's previous value. 
"""

simpleString = "Clear previous value, and assigned new value, and convert simpleNumber to a string and assign it, " \
               "value from simpleNumber is : " + str(simpleNumber)

# Print updated simpleString
print(simpleString)


"""
    Simple update a float example
"""

simpleFloat = float(100.000)  # Explicit type declaration

# Print
print(simpleFloat)

# Manipulate simpleFloat
simpleFloat = "Hi, gonna replace it with a String"  # No explicit type declaration

# Print manipulated simpleFloat
print(simpleFloat)


