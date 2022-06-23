"""
    This example going to show you how to create a programme entry point, called main function
    to execute a python programme. This example is simple.

    This example also cover command line arguments from 'sys.argv' module, while executing a python programme,
    is used to extract command line argument

    This hands-on example going to show you, how to extract command line arguments.


    For example, run a python module run with following command ->

    python test.py --message or -m <message-simple>, so you might need to get <message-simple> object from argument.
    So, keep following, you will be able to extract this value


"""

# This function will be called when this program is start
import optparse
import sys


def main_function():
    # Print a basic msg
    print("Entered in main programme")


# Main function with args
def main_function_with_args(args):
    # Simply print args
    print("The argument is received is -> %s " % args)

    # Create parser instance
    parser = optparse.OptionParser()

    # add parse option
    parser.add_option('-m', '--message',
                      action="store", dest="message",
                      help="A simple message", default="null")

    # parse all command line args
    options, arg = parser.parse_args()

    # Print -m or --message arg value, from attribute 'message'
    print('Args for -m or --message are ->', options.message)


# check for programme entry execution
# the value we compare with name, will be '__main__' if it's exacted as standalone program
# else, the '__name__' variable will have its module name
if __name__ == "__main__":
    # execute main function(no args)
    main_function()
    # execute main function(with args)
    main_function_with_args(sys.argv)
