"""
*Imprlementing Productivity System*


This program should also track employee productivity.

We need to have employee roles:
    - Manager: Salary,
    - Secretary: Salary
    - Sales People: salary and commission
    - Factory Workers: hourly


Need to move some existing code into a new file:
    - The employee classes are getting moved to a new file employees.py
    - had to update references

Now we added four new classes one for each type of worker that inherits from
another class and only adds a work() method

Next we created an productivity system in a new file called productivity.py
"""
from InheritanceAndComposition.HR import PayrollSystem
from InheritanceAndComposition import employees, productivity


manager = employees.Manager(1, 'John Smith', 1500)
secretary = employees.Secretary(2, 'Jane Doe', 1200)
salesman = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Pete Peterson', 40, 15)

employees = [
    manager,
    secretary,
    salesman,
    factory_worker
]

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
