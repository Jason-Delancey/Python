#The program is just used as practice problems in chapter 8 of 
#Python Crash Course, Eric Matthes
#functions, modules
#by Jason Delancey

#import a different module to use the functions defined in it
#you can also import individual functions from a module
#you can also use aliases when importing

import functions #have to use dot notation
from functions import * #dont have to use the dot notation now
from functions import make_pizza as mp

functions.make_pizza(16, 'pepperoni')
functions.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print()

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
print()