"""
What are these different method types good for

Comments on each method type
    - 'plain'
        - has to be called with an instance of the class

    - @classmethod
        - an be called on the class itself
            - Myclass.classmethod()

    - @staticmethod
        -
"""

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()

# instance of the MyClass object
print(obj.method())

# have access to the class but not an object of type MyClass
print(obj.classmethod())
print(MyClass.classmethod())


print(obj.staticmethod())
print(MyClass.classmethod())