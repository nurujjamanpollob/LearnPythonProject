"""
    This example going to show you how to use python assigment operator to assign value to a variable

    This example going to use integer for quick example
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

""""
    Bitwise and example, which is intended to work with two equal binary representation
    and perform the 'logical and' operations in corresponding bits.
    
    For example, there are bits for number 5(decimal) and number 3(decimal) are:
    
    * 0101 (5)
    * 0011 (3)
    
    So the operation compare each bit, if both of two compared position are 1, then the resulting binary representation
    is (1 * 1) = 1, otherwise ( 0 * 1 ) or (1 * 0) or (0 * 0) = 0 should be zero
    
    So, if we compare (5 & 3) -> 0101
                                 0011
    _________________________________________
                         Result: 0001 and 1 in decimal      
                            
    This example used 'bitwise and' -> '&=' assigment operator                        
    
"""

# Perform bitwise & operation on two integer
var &= 3

# Print
print(var)

# Replace var value
var = 5

""""
    Bitwise or example, which is intended to work with two equal binary representation
    and perform the 'logical inclusive or' operations in corresponding bits.

    For example, there are bits for number 5(decimal) and number 3(decimal) are:

    * 0101 (5)
    * 0011 (3)

    So the operation compare each bit, if both of two compared position are 0, then the resulting binary representation
    is 0, otherwise it is 1

    So, if we compare (5 & 3) -> 0101
                                 0011
    _________________________________________
                         Result: 0111 and 7 in decimal      

    This example used 'bitwise or' -> '|=' assigment operator                        

"""

# Perform bitwise or operation on two integer
var |= 3

# Print
print(var)

# Replace var value
var = 5

""""
    Bitwise xor example, which is intended to work with two equal binary representation
    and perform the 'logical exclusive or' operations in corresponding bits.

    For example, there are bits for number 5(decimal) and number 3(decimal) are:

    * 0101 (5)
    * 0011 (3)

    So the operation compare each bit, if both of two compared position are different, it will be 1, 
    otherwise, it will be 0 if both bit are either  0 and 0 or 1 and 1

    So, if we compare (5 & 3) -> 0101
                                 0011
    _________________________________________
                         Result: 0110 and 6 in decimal      

    This example used 'bitwise xor' -> '^=' assigment operator                        

"""

# Perform bitwise xor operation on two integer
var ^= 3

# Print
print(var)

# Replace var value
var = 5


"""
    Bitwise shifting - shift bit by left operand(signed) example
    
    You may know Integer stored in memory as a series of bits.
    
    For instance, the number 5 stored as a 8 bit Integer in memory will be:
                                                                           0000 0101
    Shifting this bit pattern by one left position would be result like this:
                                                                           0000 1010 -> 10 in decimal
    Okay, lets shift the bit pattern by 2 position from left, and see what is going to happened:
                                                                           0001 0100 -> 20 in decimal
                                                                           
    This example usage 'bitwise left shift' -> '<<=' assignment operator
    
"""

# Perform bitwise left operation, shift two bit from right to left
var <<= 2

# Print
print("left shift 2 bit from 5 binary bit produced output -> %d" % var)

# Replace var value
var = 5

"""
    Bitwise shifting - shift bit by right operand(signed) example

    You may know Integer stored in memory as a series of bits.

    For instance, the number 5 stored as a 8 bit Integer in memory will be:
                                                                           0000 0101
    Shifting this bit pattern by one right position would be result like this:
                                                                           0000 0010(lose one bit) -> 2 in decimal
    Okay, lets shift the bit pattern by 2 position from right, and see what is going to happened:
                                                                           0000 0001(lose two bit) -> 1 in decimal

    This example usage 'bitwise right shift' -> '>>=' assignment operator

"""

# Perform bitwise right operation, shift two bit from left to right
var >>= 2

# Print
print("right shift 2 bit from 5 binary bit produced output -> %d" % var)

"""
    Matrix multiplication example.
    
    This example going to cover matrix multiplication by a number or or by another matrix.
    
    This example gonna cover two basic and simplest example:
    
    Example one -> Matrix m where it has two row and three col like below, and multiply this matrix with 2 will result:
    
                                                                      |     | 2, 5, 3 |
                                                                  m = | 2 * | 4, 6, 1 |
                                                                      |     | 3, 6, 2 |
                                                                      _________________
    Expressions 1 row and col -> 2 * 2 = 4, 2 * 5 = 10, 2 * 3 = 6 so ->     | 4, 10, 6 |
    Expressions 2 row and col -> 2 * 4 = 8, 2 * 6 = 12, 2 * 1 = 2 so ->     | 8, 12, 2 | = updatedMatrix
    Expressions last row and col -> 2 * 3 = 6, 2 * 6 = 12, 2 * 2 = 4 ->     | 6, 12, 4 |  
                                                                           
    So, you see, it's easy to do matrix multiplication with a single number and a matrix.
    
    
    Example two -> Matrix m and Matrix n, which is has same 3 row and 2 col, like below, we need to do dot product,
    For example, follow this example: 
    
    
                                               | 2, 4 |     | 4, 5 |       
                                         m =   |      |  *  |      | = n
                                               | 4, 2 |     | 6, 3 | 
                                               
    There are possible four expression, that are given below:
    
    Expression one -> (2, 4) . (4, 6) = (2 * 4) + (4 * 6) = 8 + 24
                                                          =   32 so -> | 32, * |
                                                                       | *,  * |
                                                                    
    Expression two -> (2, 4) . (5, 3) = (2 * 5) + (4 * 3) = 10 + 12
                                                          = 22 so -> | 32, 22 |
                                                                     | *,   * |
                                                                     
    Expression three -> (4, 2) . (4, 6) = (4 * 4) + (2 * 6) = 16 + 12
                                                            = 28 so -> | 32, 22 |
                                                                       | 28,  * |
                                                                       
    Last expression -> (4, 2) . (5, 3) = (4 * 5) + (2 * 3) = 20 + 6
                                                           = 26 so -> | 32, 22 |
                                                                      | 28, 26 |
                                                                      
                                        | 32, 22 |
    So, the final output should be ->   |        |                    
                                        | 28, 26 |
                                        
    
    This usages mathematics function 'matmul' -> '@=' assigment example. The example will be updated later
                              
"""
