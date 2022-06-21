"""
    This topic introduces python modules and packages

    This lesson will go to show you how to create modules and packages, import and use it

    Python module is a file with '.py' extension, where package means multiple modules in an under directory or name
    which is mean package.

    This example going to introduce a simple module from directory -> simplemodule/SimpleModule
    where 'simplemodule' is the package, and SimpleModule is the module

    And we are good to go with it, to experiment everything. So, you maybe surprised to see a file named '__init__.py'
    This empty file is used as a package identifier.

"""

# import module from simplemodule package as the name of simpleModule
# This import a single module with all objects

import simplemodule.SimpleModule as simpleModule

# Import a function from a module example
# From module -> 'simplemodule.ModuleObjectImport' it imports a single object, which is a function get_simple_variable
# and give it a name of smp_function
from simplemodule.ModuleObjectImport import get_simple_variable as smp_function

# Import a variable from a module example
# From module -> 'simplemodule.ModuleObjectImport' it imports a single object, which is a variable simpleVariable
# and give it a name of obj_var
from simplemodule.ModuleObjectImport import simpleVariable as obj_var

# Import a class from a module example
# From module -> 'simplemodule.ModuleObjectImport' it imports a single object, which is a class 'ClassInsideModule'
# and give it a name of class_inside_module
from simplemodule.ModuleObjectImport import ClassInsideModule as class_inside_module

# Import a whole package(Including modules example)
# and give it a name of full_module
import simplemodule as full_module

# import all module object example
from simplemodule.SimpleModule import *

# Access simple function from simplemodule.SimpleModule
print("Value returned from module method -> 'simplemodule/SimpleModule.py' is %d"
      % simpleModule.calculate_absolute(-94))

# Access single function from simplemodule.ModuleObjectImport.get_simple_variable that is imported as name of
# smp_function
print("Import a single function from module -> simplemodule.ModuleObjectImport outputs -> %s " % smp_function())

# Access single variable from simplemodule.ModuleObjectImport.simpleVariable that is imported as name of
# obj_var
print("Import a single variable from module -> simplemodule.ModuleObjectImport outputs -> %s " % obj_var)

# Access single variable from simplemodule.ModuleObjectImport.ClassInsideModule that is imported as name of
# class_inside_module
# Example going to access this class's inner variable
print("Import a single class from module -> simplemodule.ModuleObjectImport , "
      "accessing it's inner variable myAge outputs -> %s " % class_inside_module.myAge)

# Access single variable from simplemodule.ModuleObjectImport.ClassInsideModule that is imported as name of
# class_inside_module
# Example going to access this class's inner method
print("Import a single class from module -> simplemodule.ModuleObjectImport , "
      "accessing it's inner method get_my_age() outputs -> %s " % class_inside_module.get_my_age(
       self=class_inside_module()))

# Access a Module from package import example
print("Now accessing a module from full package import, this example gonna print some module information -> %s "
      % full_module.SimpleModule)

# Access a single object from a module all object import
# This example going to print a method return value from simplemodule.SimpleModule.calculate_absolute(number)
print("Accessing a module function object from import simplemodule.SimpleModule.* -> %s " % calculate_absolute(-95))

# This example going to show you, which functions are implemented in each module by using dir function
print(dir(full_module))

