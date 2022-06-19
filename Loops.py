"""
    Python loops example

    Example will cover ->
     * for loop
     * while loop
     * break statement
     * continue statement
"""

# For loop example - The for loop iterate over a given sequence, here is example:
numbers = [1, 2, 3, 4, 5, 6]

# Print each number from given array
for number in numbers:
    print("Number is -> %d" % number)

# As you can understand, there are one thing is missing, maybe an index number?
# Yes, sometime it is very useful to have index number for some needs
# This example going to show you, how to get index number

index = 0

for number in numbers:
    print("Number is -> %d and index is -> %d " % (number, index))
    index += 1

# Using enumerate function to do same thing

for indx, number in enumerate(numbers):
    print("Number is -> %d and index is -> %d " % (number, indx))

# While loop example, while loop run until and boolean condition is true
count = 100

# While count value is not zero!
while count != 0:
    print("Count is decremented to -> %d" % count)
    count -= 1

# Break statement example - break statement is used to close a 'while' or 'for' loop
count = 100

# This loop continues until the count value is reached 0, if there is no break is used
while count >= 0:

    # end this loop when the count is reached 50
    if count == 50:
        print("Count reached to %d so ending it" % count)
        break
    # Else print and decrement count
    print("Count is decremented to -> %d" % count)
    count -= 1

# End a for loop
for number in numbers:
    # If number match 7 then break the loop
    if number == 7:
        print("The number is 7 so ending the for loop")
        break
    # Else print only
    print(number)

# Usages of 'continue' statement - 'continue' is used to skip a current block, while run loop
# This example going to show you how to print odd number from an integer range
for odd in range(100):
    # Check if number is even
    if odd % 2 == 0:
        # Skip current block
        continue

    # odd number
    print(" This is odd number -> %d " % odd)
