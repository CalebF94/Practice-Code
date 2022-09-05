"""
*AVOIDING THE DIAMOND PROBLEM*

Currently, we have essentially 4 program files
    1) Program.py (Each video notes page effectively mimics this file
    2) HR.py: define classes for payroll policies
    3) productivity.py: define classes for employee roles
    4) employees.py: define a class for each type of employee, which inherits from a
        payroll policy and an employee role


For this video we had to reconfigure all the files. I created an new employees2.py
file rather than ruining all other notes files

We
"""


from InheritanceAndComposition.HR import PayrollSystem
from InheritanceAndComposition import employees2, productivity


manager = employees2.Manager(1, 'John Smith', 1500)
secretary = employees2.Secretary(2, 'Jane Doe', 1200)
salesman = employees2.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees2.FactoryWorker(4, 'Pete Peterson', 40, 15)
temp_secretary = employees2.TemporarySecretary(5, 'Robin Williams', 40, 9)

employees = [
    manager,
    secretary,
    salesman,
    factory_worker,
    temp_secretary
]

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)