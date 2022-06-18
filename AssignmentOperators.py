"""
    This example going to show you how to use python assigment operator to assign value to a variable

    This example going to use integer and float for quick example
"""

var = 100  # Create simple var

var += 100  # Increment var value by 100 using '+=' assignment operator

# Print
print(var)

# Replace var value
var = 200

# Subtract example, where var has value of 200
# We are going to subtract 100 from it, using '-=' assignment operator
var -= 100

# Print
print(var)

# Replace var value
var = 100

# Multiply example, where var has value of 100
# We are going to multiply its current value with 3, using '*=' assignment operator
var *= 3

# Print
print(var)

# Replace var value
var = 300

# Divide example, where var has value of 300
# We are going to divide its current value with 3, using '/=' assignment operator
var /= 3

# Print
print(var)

# Replace var value
var = 50

# Modulus / Remainder example, where var has value of 50
# We are going to divide its current value, and divide it with 3, using '%=' assignment operator
var %= 3

# Print
print(int(var))

# Replace var value
var = 100

# Divide example, where var has value of 100
# We are going to do floor division of its current value with 2, using '//=' assignment operator
var //= 2

# Print
print(var)

# Replace var value
var = 5

# Exponent / Power example, where var has value of 5
# We are now going to pow 5 with 3, using '**=' assignment operator
var **= 3

# Print
print(var)

# Replace var value
var = 5

# Going to do pow using alternative method
var ^= 3

# Print
print(var)

# Replace var value
var = 5

""""
    Bitwise and example, which is intended to work with two equal binary representation
    and perform the logical and operations in corresponding bits.
    
    For example, there are bits for number 5(decimal) and number 3(decimal) are:
    
    * 0101 (5)
    * 0011 (3)
    
    So the operation compare each bit, if both of two compared position are 1, then the resulting binary representation
    is (1 * 1) = 1, otherwise ( 0 * 1 ) or (1 * 0) or (0 * 0) = 0 should be zero
    
    So, if we compare (5 & 3) -> 0101
                                 0011
    _________________________________________
                            Result: 0001 and 1 in decimal      
                            
    This example used bitwise and '&=' assigment operator                        
    
"""

# Perform bitwise & operation on two integer
var &= 3

# Print
print(var)

# Replace var value
var = 5

""""
    Bitwise or example, which is intended to work with two equal binary representation
    and perform the logical inclusive or operations in corresponding bits.

    For example, there are bits for number 5(decimal) and number 3(decimal) are:

    * 0101 (5)
    * 0011 (3)

    So the operation compare each bit, if both of two compared position are 0, then the resulting binary representation
    is 0, otherwise it is 1

    So, if we compare (5 & 3) -> 0101
                                 0011
    _________________________________________
                            Result: 0111 and 7 in decimal      

    This example used bitwise and '|=' assigment operator                        

"""

# Perform bitwise & operation on two integer
var |= 3

# Print
print(var)

# Replace var value
var = 5
