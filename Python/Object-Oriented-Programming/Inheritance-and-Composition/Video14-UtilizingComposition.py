"""
*Utilizing Composition

We've already been using composition
    - id and name in Employee are technically composition

We will make a new class called address that will be stored in the Contacts module
    - This module has a Address class initializer and overwrites the __str__()

We also added an address attribute to the Employee class
    - We don't assign an address at the time of initiation. The address gets
        added later

Next we modified the PayrollSystem() to print out the address if the employee
    has an address

We had to set the address of the employee after the intial instantiation
"""
from InheritanceAndComposition.HR import PayrollSystem
from InheritanceAndComposition import employees2, productivity, contacts


manager = employees2.Manager(1, 'John Smith', 1500)
manager.address = contacts.Address(
    '121 Admin Road',
    'Concord',
    'NH',
    '03301'
)

secretary = employees2.Secretary(2, 'Jane Doe', 1200)
secretary.address = contacts.Address(
    '67 Paperwork Ave',
    'Manchester',
    'NH',
    '03101'
)

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