#SDEV220 Final Project
import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, firstName:str, lastName:str, employeeID:str, wage:float, hours:float, dependents:int):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.wage = wage
        self.hours = hours
        self.grossPay = self.hours * self.wage
        self.dependents = dependents
    
    def __str__(self):
        return (f'\nFirst Name: {self.firstName} | ' +
                f'Last Name: {self.lastName} | ' +
                f'Employee ID: {self.employeeID} | ' +
                f'Dependents: {self.dependents} | ' +
                f'Payrate: ${self.wage:.2f}/hour | ' +
                f'Hours : {self.hours} | ' +
                f'Gross Pay: ${self.grossPay}\n')
    
   
class employeeList:
    def __init__(self):
        self.employees = []

    def addEmployee(self, employee: Employee):
        self.employees.append(employee)

    def deleteEmployee(self, index):
        if 0 <= index < len(self.employees):
            del self.employees[index]

    def allEmployees(self):
        return self.employees
    
    def employeeFile(self):
        with open('employees.txt', 'w') as file:
          for emplopyee in self.employees:
              temp = str(emplopyee)
              file.write(temp)
        file.close()


class employeeGUI:
    def __init__(self, root):
        self.employeeList = employeeList()
        self.root = root
        self.root.title('Employee Form')
        self.guiSetup()
    
    def label(self, text, row, column):
        tk.Label(root, text=text).grid(row=row,column=column, sticky = 'e')

    def entry(self, row, column):
        entry = tk.Entry(root)
        entry.grid(row=row,column=column, sticky = 'w')
        return entry
    
    def guiSetup(self):
        self.label("First Name:",0,0)
        self.label("Last Name:",1,0)
        self.label("Employee ID:",2,0)
        self.label("Hourly Wage ($):",3,0)
        self.label("Hours Worked:",4,0)
        self.label("Dependents:",5,0)

        self.firstName = self.entry(0,1) 
        self.lastName = self.entry(1,1)
        self.employeeID = self.entry(2,1)
        self.wage = self.entry(3,1)
        self.hours = self.entry(4,1)
        self.dependents = self.entry(5,1)

        tk.Button(self.root, text = 'Add Employee', command=self.addEmployee).grid(row=6, column=0, sticky='we')
        tk.Button(self.root, text = 'Delete Employee', command=self.deleteEmployee).grid(row=6, column=1, sticky='we')
        tk.Button(self.root, text = 'Save Info to File', command=self.saveToFile).grid(row=6,column=2, sticky='we')

        self.employeeListDisplay = tk.Listbox(self.root,width=150)
        self.employeeListDisplay.grid(row=7,column=0, columnspan=3, pady=25, sticky='we')

    def addEmployee(self):
        firstName = self.firstName.get().title()
        lastName = self.lastName.get().title()
        employeeID = self.employeeID.get()
        wage = float(self.wage.get())
        hours = float(self.hours.get())
        dependents = float(self.dependents.get())

        employee = Employee(firstName, lastName, employeeID, wage, hours, dependents)
        self.employeeList.addEmployee(employee)
        self.employeeListDisplay.insert(tk.END, employee)
        self.clearEntrys()
    
    def deleteEmployee(self):
        selected = self.employeeListDisplay.curselection()
        index = selected[0]
        self.employeeList.deleteEmployee(index)
        self.updateEmployeelistbox()
        self.clearEntrys()
    
    def saveToFile(self):
        self.employeeList.employeeFile()

    def updateEmployeelistbox(self):
        self.employeeListDisplay.delete(0, tk.END)
        for employee in self.employeeList.employees:
            self.employeeListDisplay.insert(tk.END, str(employee))
    
    def clearEntrys(self):
        self.firstName.delete(0,tk.END) 
        self.lastName.delete(0,tk.END)
        self.employeeID.delete(0,tk.END)
        self.wage.delete(0,tk.END)
        self.hours.delete(0,tk.END)
        self.dependents.delete(0,tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    employeeTracker = employeeGUI(root)
    root.mainloop()
