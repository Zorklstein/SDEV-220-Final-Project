#SDEV 220 Final project
import tkinter as tk
from tkinter import messagebox

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
    
def submit():
    first, last = first_entry.get(), last_entry.get()
    emp_id, wage, depend = id_entry.get(), wage_entry.get(), dep_entry.get()

    if not all([first, last, emp_id, wage, depend]):
        return messagebox.showwarning("Error", "Please fill out all fields.")

    try:
        emp = Employee(first, last, emp_id, wage, depend)
    except ValueError:
        return messagebox.showerror("Error", "Wage and Dependents must be numbers.")

    show_info(emp)

def show_info(emp):
    win = tk.Toplevel(root)#This code opens up the new window where employee info is displayed 
    win.title("Employee Info")#This code sets the windows title to what appears on the title bar 
    win.geometry("300x220")#This code sets the size of the window
    win.config(bg="white")#This code sets the background to white 

    #This code creates the header label at the top of the popup window 
    tk.Label(win, text="Employee Information", fg="black", bg="white",
             font=("Arial", 12, "bold")).pack(pady=8)
    tk.Label(win, text=str(emp), fg="black", bg="white", justify="left",
             font=("Arial", 10)).pack(padx=10, anchor="w")
    #This code is the close button 
    tk.Button(win, text="Close", command=win.destroy,
              bg="#4CAF50", fg="black", padx=8, pady=3).pack(pady=10)
#This code is the Main Window Setup 
root = tk.Tk()
root.title("Employee Form")
root.geometry("350x350")
root.config(bg="#f0f0f0")
root.resizable(False, False)
#This code makes the make_label function 
def make_label(text):
    tk.Label(root, text=text, bg="#f0f0f0", fg="black").pack()
#This code creates the inputs for all the employee fields 
make_label("First Name:")
first_entry = tk.Entry(root, width=35, fg="white"); first_entry.pack()

make_label("Last Name:")
last_entry = tk.Entry(root, width=35, fg="white"); last_entry.pack()

make_label("Employee ID:")
id_entry = tk.Entry(root, width=35, fg="white"); id_entry.pack()

make_label("Hourly Wage ($):")
wage_entry = tk.Entry(root, width=35, fg="white"); wage_entry.pack()

make_label("Number of Dependents:")
dep_entry = tk.Entry(root, width=35, fg="white"); dep_entry.pack()
#This code makes the submit button 
tk.Button(root, text="Submit", command=submit,
          bg="#4CAF50", fg="black", padx=10, pady=5).pack(pady=20)

root.mainloop()

