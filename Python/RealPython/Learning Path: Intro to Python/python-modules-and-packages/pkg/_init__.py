# This is used for package initialization code
print(f'Invoking __init__.py for {__name__}')
import pkg.mod1, pkg.mod2

# also has a global variable
alist = ['spam', 'bacon', 'eggs']
