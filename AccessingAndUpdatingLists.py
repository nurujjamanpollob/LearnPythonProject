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

"""
    Python list concatenating and repeating
"""

# Create concatenable list
listConcatRepeating = [1, 2, 3]

# Concat another array
listConcatRepeating += [4]

# Print updated list
print("This list updated to -> %s" % str(listConcatRepeating))

# Repeat this list for 3 time
listConcatRepeating *= 3

# Print updated list
print("This list updated to -> %s" % str(listConcatRepeating))

"""
    Python List insert example - Insert a element or another list of elements at given index
"""

# Create an insertable list
listInsertable = [1, 2, 3, 4]

# Insert 5 at index 4(last index + 1) so it's going to get a new index number
listInsertable.insert(4, 5)

# Print updated list
print("This list updated to -> %s" % str(listInsertable))

# Insert 0 at beginning index so other element index increased by +1
listInsertable.insert(0, 0)

# Print updated list
print("This list updated to -> %s" % str(listInsertable))

# Insert a list of element at given index range 0 - 6(End range is exclusive) so the whole array will get replaced
listInsertable[0:6] = [1, 1, 2, 2]

# Print updated list
print("This list updated to -> %s" % str(listInsertable))

# We're going to replace 1,1 from list with 0, 1
listInsertable[0:2] = [0, 1]

# Print updated list
print("This list updated to -> %s" % str(listInsertable))

"""
    Python delete items from list example
"""

# Create deletable list
listDeletable = [1, 2, 3, 4, 5]

# delete element at given index, the delete index is exclusive
listDeletable.remove(5)

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Alternative method to remove element from a list, delete index is inclusive
del listDeletable[3]

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Another way to remove an element from list, delete index is inclusive
listDeletable.pop(2)

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Let's restore deleted content for this list
listDeletable.extend([3, 4, 5])

# We are going to remove elements from a given index range, delete index is exclusive
del listDeletable[0:3]

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Add a str for test
listDeletable.append('f')

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Delete an element from the list, not by index but by item match
listDeletable.remove('f')

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Use pop method to remove last element from the list
listDeletable.pop()

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Use clear method to clear a list
listDeletable.clear()

# Print updated list
print("This list updated to -> %s" % str(listDeletable))

# Delete a list - If you try to access it, it will throw this error: name 'listDeletable' is not defined
del listDeletable

"""
    List count method example - return the number of occurrence present in a 
    list with given object
    
    For example, consider list = [1, 1, 2, 3, 4, 5] if we pass list.count(1) it should return 2
    because the number 1 is presented two time in this list.
"""

# Create a simple list
listSimpleCount = [1, 1, 2, 3, 4, 5]

# Print Occurrence count
print("The 1 is presented in this list for %s times" % str(listSimpleCount.count(1)))


"""
    List copy example - use copy() call to copy a list to another list
"""

# Create a copyable list
listCopy = [1, 2]

# Create another list to copy content from listCopy and assign it to new one
listCopied = listCopy.copy()

# Print updated list
print("This list copied to -> %s" % str(listCopied))

# Now, lets do selective copy and paste from one list to another
selectiveCopyPaste = [4, 3, 'placeholder']

# Print
print("The initial list is -> %s" % str(selectiveCopyPaste))

# Using Slicing operator to do copy and paste in selective index range
selectiveCopyPaste[2:3] = listCopy.copy()

# Print updated list
print("The updated list is -> %s" % str(selectiveCopyPaste))
