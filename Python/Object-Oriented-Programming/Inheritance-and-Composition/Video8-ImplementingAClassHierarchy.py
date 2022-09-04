"""
*IMPLEMENTING A CLASS HIERARCHY*

Throughout the rest of the course we will implement a project to help  an HR department.
This video had us create a file called "HR.py"

Interface:
    had to have id, name, and calculate_payroll()

Classes in HR.py

PayrollSystem:
    - Calculates the payroll for all employees
    - No attributes
    - 1 method: that calculates pay for all employees entered

Employee:
    - Base class, so it doesn't inherit from anything other than the Object class

SalaryEmployee:
    - Derived from Employee
    - the attributes for id and name are initiated using the __init__ method of
        the parent class
            - super().__init__ is what causes this
            - We still had to assign an attribute for the weekly_payroll() method to
                ensure the class conforms with the interface
    - The method weekly_payroll() just returns the weekly_salary for each employee

HourlyEmployee
    - Fairly similar to SalaryEmployee
    - have an hourly rate and hours worked attribute
    - weekly_payroll returns rate times hours worked
    - fairly straitforward

CommissionEmployee
    - This class has an interesting implementation for weekly_payroll
    - Originally, I wanted to just return commission + weekly_salary
        - The problem with this is that we want the salary part of the pay to be
            identical to the implementation that we use in the SalaryEmployee
        - To do this we created a variable called fixed that calls the weekly_payroll
            from SalaryEmployee
                - Now if we make a change in the way we calculate the weekly salary it
                only has to be changed once
"""

from InheritanceAndComposition import HR

salary_employee = HR.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HR.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = HR.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

payroll_system = HR.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])
