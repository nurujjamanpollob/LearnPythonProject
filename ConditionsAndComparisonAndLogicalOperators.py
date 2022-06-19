"""
    Python conditions.

    Python usages boolean expression to evaluate a condition.
    A True or False is returned when an expression is being compared or evaluated.

    This section also going to cover logical and comparison operator usages, and their functions.
"""

# In this example, we are going to use comparison equal '==' operator
# To evaluate a simple condition

# Create a simple condition (if / else)
# It should execute else statement
if 1 == 2:

    print("1 equals 2")

else:
    print(" 1 is not equals 2")

# Create a simple condition (if / else)
# It should execute if statement

if 1 == 1:

    print("1 equals 1")

else:
    print(" 1 is not equals 1")

# Create a condition (if/elif/else) to evaluate an expression
# This example going to cover usages of comparison grater than '>' operator
# It should execute elif statement
# create a simple variable
varX = 10

if 9 > varX:

    print("Executed if statement")

elif 11 > varX:

    print("Executed elif statement")  # This statement will be executed

else:

    print("Executed else statement")

# This example is going to coverage simple
# if statement with usages of comparison '<' less than operator

if varX < 11:
    print(" %d is less than 11" % varX)

# In this example, is going to cover a simple if statement with usages of
# comparison '<=' less then or equal to operator

if varX <= 11:

    print(" %d is less then or equal to 11" % varX)


# In this example, is going to cover a simple if statement with usages of
# comparison '>=' more then or equal to operator

if varX >= 9:

    print(" %d is more then or equal to 9" % varX)

# In this example, is going to cover a simple if statement with usages of
# comparison '!=' not equal operator

if varX != 9:

    print("definitely varX is not 9!")

# This example going to cover logical operator 'and' to evaluate two or more than two
# Boolean expression, if all expression matches true, it should return true, otherwise false
# This example is going to evaluate an if statement, which all sub-condition evaluate true.

if varX > 9 and varX < 11 :

    print('definitely varX is 10!')

# This example going to cover logical operator 'or' to evaluate two or more than two
# Boolean expression, if one of single statement is true, it should return true, if all statement
# is false, it returns false
# This example is going to evaluate an if statement, it has three condition, one statement is true only
# So it should return true
if varX > 10 or varX < 9 or varX == 10:

    print(" The varX is either greater than 10 or less than 9 or equal to 10")

# Second test, all condition is false, so the below code fraction never execute
if varX > 10 or varX < 9 or varX != 10:

    print("The code fraction never execute, because all or condition is false!")

# This example going to cover logical 'not' operator
# which simply used to negate a condition, for example, an expression 5 > 4 is True
# using 'not' treated it as False
# This example is going to execute a false statement, which will not execute, if you remove 'not' operator

if not varX < 9:

    print(" The varX value is %d and the comparison logic is varX < 9, "
          "but it execute because it's condition return type is negate using 'not' operator"
          % varX)

# This example going to block execution of a true statement using 'not' operator

if not varX == 10:

    print("The statement will never get executed, because it is negated!")


# This example going to show usages of 'in' operator
# The 'in' operator used if a specified object is exists in an iterable object container, such as list
simpleNumArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use in operator to check if 10 is exists in the list

if varX in simpleNumArray:

    print(" The number %d is in this list -> %s" % (varX, simpleNumArray))

# The 'is' operator to compare two object.
# Unlike '==' operator, the 'is' operator compare object, at memory address level.

# Create two identical memory address
x = [1, 2, 3]
y = [1, 2, 3]
# Get value and memory address from x and assign to z
z = x

# Compare by 'is' operator
if x is y:
    print("compared x with y with 'is' operator, and it's done by value comparison")

elif x is z:
    print("compared x with z with 'is' operator, and it's done by memory address comparison")

else:
    print("Unknown comparison")




