"""
*Composition to Change Runtime Behavior*

Inheritance: creates a tightly coupled relationship where classes heavily rely
    on one another

Composition: Creates a loosely-coupled relationship that supports changing
    runtime behavior

Suppose, requirements change and we now to support a longterm disability policy
    - employees paid 60% of paycheck if on ltd policy
    - In HR.py create a new class called LTDPolicy
        - Multiple methods that are used to return 60% of employees pay if the
            policy is LTD

    - Added method to Employee class that takes in a new policy and applies it to
        the employee
"""

import json
from HR import calculate_payroll, LTDPolicy
from productivity import track
from employees2 import employee_database, Employee


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees()

sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)

track(employees, 40)
calculate_payroll(employees)