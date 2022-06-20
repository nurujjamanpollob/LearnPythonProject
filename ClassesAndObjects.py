"""
    Classes and Objects in python

    Classes or class is like a template to create objects.
    And object is an encapsulation of functions and variables into a single entity.

    Object inherits their function and variable from class or classes.

    This example is going to cover, how to create classes, objects and update and accessing variables of Object or class

"""


# Create a simple class with a variable and function
class SimpleClass:
    # Create an inner variable
    name = "Nurujjaman Pollob"

    # Create a simple function to get name with a customized message
    # 'self' is needed for instance access
    def get_name(self):
        # return name
        return "Hi, my name is %s " % self.name


# Create an object of SimpleClass
simpleObj = SimpleClass()

# Accessing object variable
print("Accessing SimpleClass object variable -> %s " % simpleObj.name)

# Accessing a function of SimpleClass object
print("Accessing a function of SimpleClass -> %s " % simpleObj.get_name())

"""
    The init function - is a special function, that is called the class is being initialized.
    You can use it to assigning values in a class.
    
    Now this example, going to leverage it.
"""


# Create a simple class with init function
class SimpleClassWithInit:
    age = 0

    # This method going to replace age variable value
    def __init__(self):
        # Replace age variable value at init level
        self.age = 22


# Create a simple object instance
simplObj = SimpleClassWithInit()

# Access age variable from simplObj
print("Accessing a variable of SimpleClassWithInit -> %s" % simplObj.age)
