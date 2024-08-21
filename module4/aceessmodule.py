import sys
locations = sys.path
print(locations)
for i in locations:
    print(i)


import calendar

leapdays = calendar.leapdays(2000 , 2050)
print(leapdays)

isit_leap = calendar.isleap(2036)
print(isit_leap)

# we can import the other file in our main module for example:
# the import usecase file are other file which is import in acessmodule.py
# if some package are not found in the pycharm you can download package by (pip install numpay, seaborn etc.

import usecase

print("import usecase file:")

import math

 # by import math taking square root
root = math.sqrt(9)
print("The squareroot of 9 is :" , root)


# another way to do the above square function by math package

from math import sqrt
 # by import math taking square root
root = sqrt(9)
print("The squareroot of 9 is :" , root)

# Here I sign an alias called m to the from math import sqrt module. I do this by typing from math import sqrt as m.

from math import sqrt as m
 # by import math taking square root
root = m(9)
print("The squareroot of 9 is :" , root)


# we can use ( form math import *) to import all the functions of math init

from math import *

root = factorial(10)
print("The factorial of 9 is :" , root)
soot = sqrt(9)
print("The squareroot of 9 is :" , soot)


# There are four main types of scopes that can be defined in Python: local, enclosed, global and built-in.
# The practice of trying to determine in which scope a certain variable belongs is known as scope resolution.
# Local, this is where the first search for a variable is in the local scope.
# Enclosed, this is defined inside an enclosing or nested functions.
# Global is defined at the uppermost level or simply outside functions,
# and built-in,which is the keywords present in the built-in module.


def a():
    animal = "elephant"
    def b():
        nonlocal  animal
        animal = "lion"
        print("inside nested function: " + animal)
    print("before calling  function: " +animal)
    b()
    print("after nested function:" + animal)
animal = " camel"
a()
print("Global animal:" + animal)