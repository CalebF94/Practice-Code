from productivity import get_role
from HR import get_policy
from contacts import get_employee_address
from representations import AsDictionaryMixin


class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2: {
                'name': 'John Smith',
                'role': 'secretary'
            },
            3: {
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4: {
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5: {
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        }

    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError('invalid employee_id')
        return info


class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get('name')
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get('role'))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.work(hours)
        print(f'Employee {self.id} - {self.name}')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    # takes in new policy to apply
    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


# video 19 additions:
employee_database = _EmployeeDatabase()


#
# # all the following classes will first inherit from Employee then from productivy role
# # the from payroll
# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name) # will stop at Employee class
#
#
# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)
#
#
# class SalesPerson(Employee, SalesRole, CommissionPolicy):
#     def __init__(self, id, name, weekly_salary, commission):
#         CommissionPolicy.__init__(self, weekly_salary, commission)
#         super().__init__(id, name)
#
#
# class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)
#
#
# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)