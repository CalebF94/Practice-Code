"""
*MULTIPLE INHERITANCE*

Multiple Inheritance:
    - This allows one class to derive from multiple other classes
    - We may want to use this if we add a temporary secrectary that uses the work from
        the secretary but gets paid like an hourly employee

MRO:
    - Method Resolution Order
    - A set of rules that defines the search path that Python uses when searching for
        a method in cases of inheritance
    - Looks like an ordered list of classes
    - Each class has its own MRO
    - Used by the super() function
    - use classname.__mro__ to see the MRO

The Diamond Problem
    - Occurs when a class inherits from two parent classes that inherite from the same
        class higher in the hierarchy
    - You can typically apply a quick fix, but usually this means it is time to
        rethink the layout of your program
"""

from InheritanceAndComposition.HR import PayrollSystem
from InheritanceAndComposition import employees, productivity


manager = employees.Manager(1, 'John Smith', 1500)
secretary = employees.Secretary(2, 'Jane Doe', 1200)
salesman = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Pete Peterson', 40, 15)
temp_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)

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