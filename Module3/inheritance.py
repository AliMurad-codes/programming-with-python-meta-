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