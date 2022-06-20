"""
    This topic introduces about python functions,
    functions means a useful set of code block to divide your code
    and accomplish and organize your code and goal.

    Now, I am going to write some functions, to show you some example.
"""


# Create a simple function
def simple_function_print_greeting():
    print("Welcome to Python Console!\n\n")


# This function used to take a String input from the end user
# Function with return statement, the return statement is used to return object when a method execution process
# is finished
def take_input_from_user():
    return input("Input something -> ")


# call simple_function_print_greeting
simple_function_print_greeting()

# This print statement take input from user using a custom function and print it
print("The input from user -> %s \n\n" % take_input_from_user())

"""
    So you see, using functions, we can organize our code and do different task to 
    accomplish a bigger task.
    
    Let's create function with arguments, the process flow consist two user input,
    then merge those two input in a string, and print it
"""


# Show a simple message
print("Hello, you don't mind answer some basic question? \nI want to be your friend 😌\n\n")


# Take username and age input from console
def take_user_name_and_age_from_console_and_return_user_details():
    # Take name
    name = input("Please enter your name -> ")
    age = int(input("Please enter your age -> "))

    # Return simple message from user_details_message
    return user_details_message(name, age)


# Create function with argument
def user_details_message(name, age):
    # Return generated message
    return "\n\nHello, %s! You are %d years old!" % (name, age)


# Print username and age
print(take_user_name_and_age_from_console_and_return_user_details())
