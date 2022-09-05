"""
*ABSTRACT CLASSES

Notice that no objects were instantied for the base Employee classs. It only used for the
name and ID attributes from other classes

What happens if we try to instantiate a Employee and run the .calculate_payroll() method
    - We get an error saying calculate_payroll() doesn't exist for Employee
    - It only broke because we didn't run the code correctly

Abstract Class
    - A class that only exists to be inherited from, not to be instantiated
    - To utilize a helpful abstract decorater use abc module
    - In HR.py, we imported ABC and abstractmethod

In HR.py
    - we made Employee inherit from ABC
    - added @abstractmethod decorator before the calculate_payroll method
        - This changed the warning given to tell the user that this method is designed
            to be implemented in the children class
"""
from InheritanceAndComposition import HR

salary_employee = HR.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HR.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = HR.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
generic_employee = HR.Employee(4, "Generic Employee")


payroll_system = HR.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    generic_employee
])
