class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    def __init__(self, num_rooms=5, bathrooms=2):
        self.num_rooms = num_rooms
        self.bathrooms = bathrooms

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost

# Create instances of House
house1 = House(num_rooms=7)
house2 = House(num_rooms=5)

# Calculate and print the cost for both houses
rate = 15
cost_house1 = house1.cost_evaluation(rate)
cost_house2 = house2.cost_evaluation(rate)

print(f"Cost for a house with {house1.num_rooms} rooms: {cost_house1}")  # Output: 105
print(f"Cost for a house with {house2.num_rooms} rooms: {cost_house2}")  # Output: 75

class Recipe():
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time
    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
        " and takes " + str(self.time) + " min to prepare")

pizza = Recipe ("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)
print(pizza.contents())


# Define class MyFirstClass
class MyFirstClass:
    print("who wrote this?")
    # Define string variable called index
    def __init__(self, index, author_book):
        self.index = index
        self.author_book = author_book
    # Define function hand_list()
    def hand_list(self):
        print(str(self.index) + " wrote the book:" + str(self.author_book))

# Call function handlist()
myc = MyFirstClass("Ali", "python")
myc.hand_list()



# apply instance method in class

class payslips:
    def __init__(self, name , payments , amount):
        self.name = name
        self.payments = payments
        self.amount = amount
    def pay(self):
        self.payments = "yes"
    def status(self):
        if self.payments == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

py = payslips("Ali","no", 1000)
ly = payslips("Murad","yes",  1000)

print(py.status())
print(ly.status())

py.pay()
print("After payments")
print(py.status())