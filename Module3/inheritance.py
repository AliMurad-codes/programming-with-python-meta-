class employee:
    def __init__(self, name , last):
        self.name = name
        self.last = last
class supervisor(employee):
    def __init__(self, name , last, password):
        super().__init__(name, last)
        self.password = password

class chefs(employee):
    def leave_request(self, days):
        return " May i take a leave for " + str(days) + " days "

a = employee("ali" , "A")
b = chefs("Murad" , "M")

c= supervisor("fahad" , "s" , "apple")

print(b.leave_request(5))
print(c.password)
print(b.name)


inheritance

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)
