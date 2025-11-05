#SDEV 220 Final project

class Employee:
    def __init__(self):
        self.firstName = input("What is the employee's first name: ")
        self.lastName = input("What is the employee's last name: ")
        self.employeeID = input("What is the employee's ID number: ")
        self.wage = float(input("How much does the employee make per hour: "))
        self.dependents = input("How many dependants does the employee have: ")
    
    def __str__(self):
        return (f'\nFirst Name: {self.firstName}\n' +
                f'Last Name: {self.lastName}\n'+
                f'Employee ID: {self.employeeID}\n'+
                f'Payrate: ${self.wage:.2f}/hour\n'+
                f'Number of Dependants: {self.dependents}\n')
    


