# Which data structure to choose?
# The tricky part for new developers is understanding
# which data structure is suited to the required solution.
# Each data structure offers a different approach to storing,
# accessing and updating the information stored inside it.
# There can be many factors to select from, including size, speed and performance.
# The best way to try and understand which one is more suitable is through an example.

# Example: Employees list
# In this example, there's a list of employees that work in a restaurant.
# You need to be able to find an employee by their employee ID - an integer-based numeric ID.
# The function get_employee contains a for loop to iterate over the list of employees and returns an employee object if the ID matches.

employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

def get_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return {"id": employee[0], "name": employee[1], "department": employee[2]}

print(get_employee(12458))



# In this code, employee_list is a list of tuples.
# The code runs well and will return the user Paul, as its ID, 12458, is matched. The challenge comes when the list gets bigger.
# Instead of two employees, you may have 2000 or even 20,000.
# The code will have to iterate over the list sequentially until the number is matched.
# You could optimize the code to split the search, but even with this,
# it still lacks in performance in comparison to other data structures, such as the dictionary.

employee_dict = {
    12345: {
        "id": "12345",
        "name": "John",
        "department": "Kitchen"
    },
    12458: {
        "id": "12458",
        "name": "Paul",
        "department": "House Floor"
    }
    }

def get_employee_from_dict(id):
    return employee_dict[id];


print(get_employee_from_dict(12458));



# ZeroDivisionError
# In math there are rules about dividing by zero.
# below code is trying to do just that and will throw a ZeroDivisionError.
# exception handling to return back 0 instead of allowing the error to be thrown.

# Starter code
def divide_by(a, b):
    return a / b
try:
    print(divide_by(40, 0))
except Exception as e:
    print("invalid",e)

FileNotFoundError
# The code below is looking for a file that does not exist.
# Add exception handling to catch this error and return the following "The file could not be found".
# # Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("The file could not be found")