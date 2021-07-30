from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random import choice

'''FIX THIS'''

p = Player('Yure')

capture_explaination(p)

b = str(input('>>> '))

test = p.capture(Charmander, 'object_forest', b)

if test == True:
    capture_status(Charmander, p, 1)

if test == False:
    capture_status(Charmander, p, 2)

capture_explaination(p)
