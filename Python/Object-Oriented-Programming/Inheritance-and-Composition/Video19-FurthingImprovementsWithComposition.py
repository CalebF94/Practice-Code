"""
*Further Improving Design with Composition*

Composition can make certain classes become crowded.

The Factory Method
    - A class contains a method for constructing an object with the correct
        parameters
    - Ex) EmployeeDatabase._create_employee() creates Employee objects from
        information stored within the database

It would be better if we could create and employee by just suppling the id

Productivity.py changes
    - We really only need 1 productivitySystem
    - WE are going to make ProductivitySystem a singleton
        - Add _ to Class name and then create a single instance of _ProdSystem
    - Created two functions that allow the user to interact with the
        _ProductivitySystem object
    - We created a public facing interface for users of the module

HR.py and contacts.py changes
    - Made similar changes as made in Productivity.py

These changes are abstractions. We took away some of the complex inner workings
and provided the user with a more strait forward method of interaction

employees2.py changes
    - Changed import lines to only import certain functions
    - made EmployeeDatabase private by prepending with _
    - made the _EmployeeDatabase class self._employees into a dictionary of
        dictionaries where the key is the id. Removed id from the inner dictionary
    - Modified the employees() method to return a list of ids
    - Replaced _create_employee with get_employee_info

"""

import json
from HR import calculate_payroll
from productivity import track
from employees2 import employee_database, Employee


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees()

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temp Secretary')
print_dict(temp_secretary.to_dict())
