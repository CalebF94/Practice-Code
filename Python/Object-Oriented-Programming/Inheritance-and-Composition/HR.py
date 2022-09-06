from abc import ABC, abstractmethod


class _PayrollSystem:
    def __init__(self):
        # Internal database for employee policy
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError('invalid employee_id')
        return policy

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')


class LTDPolicy:
    # base policy will be the policy b4 going on LTD
    def __init__(self):
        self._base_policy = None

    # accepts hours to work and
    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    # Check base policy and if ok return 60% of base policy
    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * 0.6

    # used to change base policy
    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    # checks if base policy is None
    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError('Base policy missing')


class PayrollPolicy: # Base class for all other policies
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission()


# Video 19: Public interface for user interaction
_payroll_system = _PayrollSystem()


def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)


def calculate_payroll(employees):
    return _payroll_system.calculate_payroll(employees)

#
# class Employee(ABC):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     @abstractmethod
#     def calculate_payroll(self):
#         pass
#
#
#
# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
#
# class CommissionEmployee(SalaryEmployee):
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return self.commission + fixed