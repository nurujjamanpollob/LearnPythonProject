"""
   This example module is created to show example of import a single object from a module
"""

# Create a simple variable
simpleVariable = "Hello, I a Nurujjaman Pollob"


# Create a method
def get_simple_variable():
    return simpleVariable


# Create a class
class ClassInsideModule:
    # Define a variable inside class
    myAge = 22

    # Define a simple function
    def get_my_age(self):
        return "%s, and I am %d years old" % (simpleVariable, self.myAge)
