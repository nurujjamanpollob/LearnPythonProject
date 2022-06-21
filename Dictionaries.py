"""
    Python dictionary - a dictionary is a data type like arrays, but it stores data in key value format

    This example going to show you how to create a dictionary, add key value pair, query and update it

"""

# Create a simple dictionary
simpleDictionary = {}

# Add a simple key value pair
simpleDictionary['name'] = 'Nurujjaman Pollob'
simpleDictionary['age'] = 22

# Alternately, you can use
simpleDictionary = {

    "name": "Nurujjaman Pollob",
    'age': 22,
    'sex': "Male"
}

# Print this dictionary
print("The simple dictionary is -> %s " % simpleDictionary)


# Iterating dictionary items
for key, value in simpleDictionary.items():

    # Print key
    print("Key is -> %s" % key)
    # Print value
    print("Value is -> %s" % value)


# Iterate only keys
for key in simpleDictionary.keys():
    # Print key
    print("Key is -> %s" % key)

# Iterate only values
for value in simpleDictionary.values():
    # Print value
    print("Value is -> %s" % value)


# Removing an element (key, value) pair from list by keyname
del simpleDictionary['age']

# Print updated dictionary
print("The dictionary is updated to -> %s " % simpleDictionary)

# Remove an element by pop function
simpleDictionary.pop('sex')

# Print updated dictionary
print("The dictionary is updated to -> %s " % simpleDictionary)

