#
#
#   Python: 3.10.6
#
#
#   Author: Jacob A. Lopez
#
#
#   Purpose: The Tech Academy's Python Course.
#            Creating classes that inherit properties
#            from their parent classes.


# Creating a parent class
class User:
    name = 'No Name Provided' # An attribute that the child class will inherit
    email = ' '     # An attribute that the child class will inherit
    password = '1234abcd'   # An attribute that the child class will inherit
    account_number = 0 # An attribute that the child class will inherit

# Creating the first child class to inherit the parents properties
class Employee(User):
    base_pay_rate = 15.00  # Setting an attribute that only the child class has
    department = 'General' # Setting an attribute that only the child class has

# Creating the second child class to inherit the parents properties
class Customer(User):
    mailing_address = ' ' # Setting an attribute that only the child class has
    mailing_list = True   # Setting an attribute that only the child class has
