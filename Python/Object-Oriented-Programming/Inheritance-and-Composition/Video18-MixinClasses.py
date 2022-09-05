"""
*MIXIN CLASSES

Mixin:
    - Provides only methods to classes that derive from it
    - Not considered a base class
        - Doesn't follow the is a relationship
        - Classes only inherit from a mixin to utilize one or more of its methods

We inherit from a mixin just to utilize its methods. The mixin class is more of a
utility

We created a file called representations.py that will contain a class that other
classes will inherit from
    - AsDictionaryMixin class was created in representations
    - Modified the Employee class to inherit from AsDictionaryMixin
    - made the role and payroll attributes in Employee to _role and _payroll
"""

from HR import PayrollSystem, HourlyPolicy # imported HourlyPolicy
from productivity import ProductivitySystem
from employees2 import EmployeeDatabase
import json
#
# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees()
#
# # New lines added
# manager = employees[0]
# manager.payroll = HourlyPolicy(55)
#
#
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)


def print_dict(d):
    print(json.dumps(d, indent=2))


for employee in EmployeeDatabase().employees():
    print_dict(employee.to_dict())