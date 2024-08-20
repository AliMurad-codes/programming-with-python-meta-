# Recursion
# Recursion refers to a method or a function that will call itself.
# It is used to resolve problems by breaking the problem down into sub-problems.
# Let us take a look at some of the most popular types of recursive algorithms.
#
# Divide and conquer
# This consists of two parts.
# The first is breaking the problem down into smaller sub-problems and the second is solving the final solution.
#
# Dynamic programming
# This is mainly used for optimization problems.
#     It is similar to the divide and conquer algorithm in that it splits the problems into sub-problems.
#
# Greedy algorithm
# This one finds the best solution in each and every step instead of approaching optimization in a global way.

# tower of hanio in python

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')

# recurtion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
         return string_reverse(str[1:]) + str[0]

str = "reversal"
reverse = string_reverse(str)
print(reverse)

# without recursion solve the same problem:
a = "reversal"
b = a[::-1]
print(b)


# mapping: Let me explain the difference between a map and a filter function.
# A map takes all objects in the list and allows you to apply a function to it.
# A filter also allows you to take in all objects in the list and runs through a function
# but it creates a new list and only returns values where the evaluated function returns true.

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]
def find_coffee(coffee):
    if coffee [0] == 'c':
        return coffee
map_coffee = map (find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)


# filter
filter_coffee =  filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)