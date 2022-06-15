"""
    In this example, I'm going to access a python list element by its index.
    In python, the index starts from zero, and the index number can be found by this formula:
    (actual index - 1) = list index, for example this list -> list = [0,1], so if you want to access
    0, which is simply number 1 index in your mind, but in python it should be (1 - 1) = 0

    If you want to access 1 in this list, it should be (your index 2 - 1) = 1 number index in python.
    If you try 2 to access, it should throw a IndexError: list index out of range because there are no such index
    exists in this list
"""

# Create a simple list
simpleIterableList = ["Hi", "Welcome", "to", "Python"]  # No explicit type declaration

# Access list element 0
print("List element 0 contains -> %s" % simpleIterableList[0])

# Access list element 1
print("List element 1 contains -> %s" % simpleIterableList[1])

# Access list element 2
print("List element 2 contains -> %s" % simpleIterableList[2])

# Access list element 3
print("List element 3 contains -> %s" % simpleIterableList[3])

"""
    In this example, I gonna access a nested list, and it's element
"""

# Create a nested list
# No explicit type declaration
nestedList = ["Hi, there are student presented by roll ", [1, 5, 7, 10], "in this class"]

# Access list element 0
print("list element 0 contains -> %s" % nestedList[0])

# Access list element 1, which is a nested list
# We're going to access this nested list's index 0
print("list element 1 contains list index 0 contains -> %s" % nestedList[1][0])

# Access list element 1, which is a nested list
# We're going to access this nested list's index 1
print("list element 1 contains list index 1 contains -> %s" % nestedList[1][1])

# Access list element 1, which is a nested list
# We're going to access this nested list's index 2
print("list element 1 contains list index 2 contains -> %s" % nestedList[1][2])

# Access list element 1, which is a nested list
# We're going to access this nested list's index 3
print("list element 1 contains list index 3 contains -> %s" % nestedList[1][3])

# Access list element 2
print("list element 0 contains -> %s" % nestedList[2])

"""
    Negative index - Python allows negative index for its list element sequences
    For example, the -1 index means the last element in a list, -2 means second last element
    and so on.
    
    For example, this example -> list = [1,2,3,4] where list[-1] should return 4, list[-2] should return 3
    list[-3] should return 2 and list[-4] should return 1.
    
    If you try list[-5] it should throw a IndexError: list index out of range
"""

# Create a basic list
basicList = [1, 2, 3, 4]  # No explicit type declaration

# Access by negative index, the last index
print("Accessing list by negative index -1 returns %s" % basicList[-1])

# Access by negative index, the second last index
print("Accessing list by negative index -2 returns %s" % basicList[-2])

# Access by negative index, the third last index
print("Accessing list by negative index -3 returns %s" % basicList[-3])

# Access by negative index, the fourth last index
print("Accessing list by negative index -4 returns %s" % basicList[-4])


"""
    List slicing - accessing a range of list element
    
    For example, consider this list -> list = [1, 2, 3, 4] where list[1:3] should return [2,3],
    list[:2] should return [1, 2], list[2:] should return [3, 4] and list[:] should return full array.
    
    Note: the ending range is exclusive, you see!
    
    Trying invalid index range should throw a IndexError: list index out of range
"""

# Create a list for slicing
listSlice = [1, 2, 3, 4]  # No explicit type declaration

# Print the element index from 1 to 2(last index is exclusive)
print("list slice range from 1 to 2 element is %s" % str(listSlice[1:2]))

# Print the element index from 0 to 2(last index is exclusive)
print("list slice range from 0 to 3 element is %s" % str(listSlice[0:3]))

# Print the element index from begin to 4(last index is exclusive)
print("list slice range from begin to 4 element is %s" % str(listSlice[:4]))

# Print the element index from 2 to last
print("list slice range from 2 to last element is %s" % str(listSlice[2:]))

# Print full element using slice
print("list slice print full list %s" % str(listSlice[:]))


"""
    Updating a simple list example - We gonna create a list, and manipulate its element
"""

# Create a simple updatable list
updateList = [0, 1, 2, 3, 4]  # No explicit type declaration

# Change the element at 4th index
updateList[4] = 5

# Print updated list
print("The updated list is -> %s" % str(updateList))

# Change the element at 0th index
updateList[0] = 6

# Print updated list
print("The updated list is -> %s" % str(updateList))


"""
    Update a range of list element from a list example - We gonna create a list, 
    and update it's element at a target index range.
    
    For example this -> list = [0, 1, 2, 3, 4] and for example we gonna replace from 1 th element to 3 th element, so
    in this list it is [1, 2, 3]. So we gonna replace it with [5, 6, 7] 
    so the updated list will become [0, 5, 6, 7, 3, 4]
    
    Note: the ending range is exclusive, you see!
"""

# Create the updatable list variable
updateListRange = [0, 1, 2, 3, 4]  # No explicit type declaration

# Update the list from index 1 to 3
updateListRange[1:3] = [5, 6, 7]

# Print updated list
print("This list updated to -> %s" % str(updateListRange))

# Undo previous change
updateListRange[1:4] = [1, 2]

# Print updated list
print("This list updated to -> %s" % str(updateListRange))


# Update list from index 2 to end
updateListRange[2:] = [1, 0]

# Print updated list
print("This list updated to -> %s" % str(updateListRange))

# Update list from index begin to 3
updateListRange[:3] = [3, 2, 1]

# Print updated list
print("This list updated to -> %s" % str(updateListRange))

# Update full array with range
updateListRange[:] = [2, 3, 4, 4, 3, 2]

# Print updated list
print("This list updated to -> %s" % str(updateListRange))


"""
    Python list append and extend a list example
    Adding a element or extending list by another list always added in the end
"""

# Create extensible list
extensibleList = [1, 2, 3, 4]

# Add 5 to the list
extensibleList.append(5)

# Print updated list
print("This list updated to -> %s" % str(extensibleList))

# Extend this list
extensibleList.extend([6, 7, 8, 9, 10])

# Print updated list
print("This list updated to -> %s" % str(extensibleList))
