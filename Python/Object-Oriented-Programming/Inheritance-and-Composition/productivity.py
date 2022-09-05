class ProductivitySystem:
    def __init__(self):
        # Starting with _ tells other developers this attribute shouldn't be
        # used outside of the class. We'll have a method to give _roles info
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('invalid role_id')
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print(' ')


class ManagerRole:
    def work(self, hours):
        return f' Screams and yells for {hours} hours'


class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} doing office paperwork'


class SalesRole:
    def work(self, hours):
        return f'expends {hours} hours on the phone'


class FactoryRole:
    def work(self, hours):
        return f'expends {hours} manufacturing gadgets'