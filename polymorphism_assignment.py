#
# Python: 3.10.6
#
# Author: Jacob A. Lopez
#
#
# Purpose: The Tech Academy - Python Course, Polymorphism Assignment.


# Parent Class User
class User:
    name = "Jake"
    email = "jake@gmail.com"
    password = "Password1234"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email you've entered is incorrect.")


# Child Class Employee
class Employee(User):
    base_pay = 15.00
    department = "General"
    pin_number = "2468"

# This is the same method in the parent class "User".
# The difference is that, instead of using entry_password, i'm using entry_pin.
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email you've entered is incorrect.")


# The following code invokes the methods inside each class for User and Employee.
if __name__ == "__main__":
    customer = User()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLoginInfo()
