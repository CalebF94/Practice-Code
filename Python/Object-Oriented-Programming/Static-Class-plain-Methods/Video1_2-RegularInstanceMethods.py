"""
DIfference between @classmethod vs @staticmethod vs "plain methods

Comments on each method
    - method()
        - :plain instance method
        - can modify/read object instance state

    - classmethod()
        - only has access co cls argument
        - can't modify object instance state
        - can modify class state

    -staticmethod()
        - no arguments, no access to class or object instance
        - can't modify object instance state
        - cant modify class state
"""

class myClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'