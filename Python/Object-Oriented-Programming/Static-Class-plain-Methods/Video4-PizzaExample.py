"""
Mastering method typs with the OOP Pizza Example

WHEN TO USE CLASS METHODs
------------------------------
A good use of @classmethod is when you have some standard function calls that
are lengthy.

In the Pizza example, this amounts to creating certain types of pizza. We created
class methods that when called create a certain type of pizza
    - Pizza.margherita()
    - Pizza.prosciutto()
These methods don't get called on an instance of Pizza, but rather they get called
on the class itself


WHEN TO USE STATIC METHODS
------------------------------
Static methods have one big limitation: They don't have access to the class or the
object instance. However this shows that a static method is independent of the
things around it.


"""
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'


    #Video 5
    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['chees', 'tomatoes', 'ham', 'mushrooms'])


cm = Pizza.margherita()
print(cm)
