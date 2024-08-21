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