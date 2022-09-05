"""
*Modifying Behavior with composition*

One of the benefits of a policy based design allows us to modify behavior
    - all we have to do is change one component of one object
    - The ceo decides to take away the managers salary to $50 an hour
        - All we would have to do is add two lines of code and import HourlyPolicy
"""


from HR import PayrollSystem, HourlyPolicy # imported HourlyPolicy
from productivity import ProductivitySystem
from employees2 import EmployeeDatabase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees()

# New lines added
manager = employees[0]
manager.payroll = HourlyPolicy(55)


productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
