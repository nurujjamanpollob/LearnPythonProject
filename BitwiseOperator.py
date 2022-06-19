"""
    Bitwise operator example - the theory is same in all major programming language, but maybe
    their syntax can be different, If I am wrong correct me.

    Be sure to read it carefully, if you don't know about it.
"""

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

    This example used 'bitwise and' -> '&' operator                        

"""

# Perform bitwise & operation on two integer
simpleVar = 5 & 3

# Print
print(simpleVar)

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

    This example used 'bitwise or' -> '|' operator                        

"""

# Perform bitwise or operation on two integer
simpleVar = 5 | 3

# Print
print(simpleVar)

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

    This example used 'bitwise xor' -> '^' operator                        

"""

# Perform bitwise xor operation on two integer
simpleVar = 5 ^ 3

# Print
print(simpleVar)


"""
    Bitwise shifting - shift bit by left operand(signed) example

    You may know Integer stored in memory as a series of bits.

    For instance, the number 5 stored as a 8 bit Integer in memory will be:
                                                                           0000 0101
    Shifting this bit pattern by one left position would be result like this:
                                                                           0000 1010 -> 10 in decimal
    Okay, lets shift the bit pattern by 2 position from left, and see what is going to happened:
                                                                           0001 0100 -> 20 in decimal

    This example usage 'bitwise left shift' -> '<<' operator

"""

# Perform bitwise left operation, shift two bit from right to left
simpleVar = 5 << 2

# Print
print("left shift 2 bit from 5 binary bit produced output -> %d" % simpleVar)

"""
    Bitwise shifting - shift bit by right operand(signed) example

    You may know Integer stored in memory as a series of bits.

    For instance, the number 5 stored as a 8 bit Integer in memory will be:
                                                                           0000 0101
    Shifting this bit pattern by one right position would be result like this:
                                                                           0000 0010(lose one bit) -> 2 in decimal
    Okay, lets shift the bit pattern by 2 position from right, and see what is going to happened:
                                                                           0000 0001(lose two bit) -> 1 in decimal

    This example usage 'bitwise right shift' -> '>>' operator

"""

# Perform bitwise right operation, shift two bit from left to right
simpleVar = 5 >> 2

# Print
print("right shift 2 bit from 5 binary bit produced output -> %d" % simpleVar)

