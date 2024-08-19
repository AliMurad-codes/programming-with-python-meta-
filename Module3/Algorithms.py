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


# mapping:

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]
def find_coffee(coffee):
    if coffee [0] == 'c':
        return coffee
map_coffee = map (find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)


#
filter_coffee =  filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)