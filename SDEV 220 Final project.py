import tkinter as tk
from tkinter import messagebox

# ------- Employee class -------
class Employee:
    def __init__(self, firstName:str, lastName:str, employeeID:str, dependents:int, wage:float, hours:float):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.wage = wage
        self.hours = hours
        self.grossPay = self.hours * self.wage
        self.dependents = dependents
    
    def __str__(self):
        return (f'\nFirst Name: {self.firstName}\n' +
                f'Last Name: {self.lastName}\n'+
                f'Employee ID: {self.employeeID}\n'+
                f'Dependents: {self.dependents}\n'+
                f'Payrate: ${self.wage:.2f}/hour\n'+
                f'Hours : {self.hours}\n'+
                f'Gross Pay: ${self.grossPay}')
    
    
class employeeList:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def delete_employee(self, index):
        if 0 <= index < len(self.employees):
            del self.employees[index]

    def get_all(self):
        return self.employees
# Store employees
employees = []

# Windows
list_window = None
list_text = None


# ------- Update / Create List Window -------
def update_list_window():
    global list_window, list_text

    # Make window if not made yet
    if list_window is None or not tk.Toplevel.winfo_exists(list_window):
        list_window = tk.Toplevel(root)
        list_window.title("All Employees")
        list_window.geometry("350x400")
        list_window.config(bg="white")

        tk.Label(list_window, text="Employees:", bg="white", fg="black",
                 font=("Arial", 12, "bold")).pack(pady=5)

        frame = tk.Frame(list_window, bg="white")
        frame.pack(fill="both", expand=True)

        list_text = tk.Text(frame, width=40, height=20, bg="white", fg="black")
        list_text.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(frame, command=list_text.yview)
        scroll.pack(side="right", fill="y")
        list_text.config(yscrollcommand=scroll.set)

    # Update text
    list_text.config(state="normal")
    list_text.delete("1.0", "end")

    for emp in employees:
        list_text.insert("end", str(emp))
        list_text.insert("end", "----------------------\n")

    list_text.config(state="disabled")


# ------- Submit -------
def submit():
    first = first_entry.get()
    last = last_entry.get()
    emp_id = id_entry.get()
    wage = wage_entry.get()
    depend = dep_entry.get()

    if not all([first, last, emp_id, wage, depend]):
        return messagebox.showwarning("Error", "Please fill out all fields.")

    try:
        emp = Employee(first, last, emp_id, wage, depend)
    except ValueError:
        return messagebox.showerror("Error", "Wage and Dependents must be numbers.")

    employees.append(emp)
    update_list_window()

    # Clear fields
    first_entry.delete(0, tk.END)
    last_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    wage_entry.delete(0, tk.END)
    dep_entry.delete(0, tk.END)


# ------- Main Window -------
root = tk.Tk()
root.title("Employee Form")
root.geometry("300x350")
root.config(bg="white")

# Labels + Entry boxes
def label(text):
    tk.Label(root, text=text, bg="white", fg="black").pack(anchor="w", padx=15)

label("First Name:")
first_entry = tk.Entry(root, width=30); first_entry.pack()

label("Last Name:")
last_entry = tk.Entry(root, width=30); last_entry.pack()

label("Employee ID:")
id_entry = tk.Entry(root, width=30); id_entry.pack()

label("Hourly Wage ($):")
wage_entry = tk.Entry(root, width=30); wage_entry.pack()

label("Dependents:")
dep_entry = tk.Entry(root, width=30); dep_entry.pack()

# Submit button
tk.Button(root, text="Submit", command=submit,
          bg="#4CAF50", fg="black").pack(pady=15)

root.mainloop()
