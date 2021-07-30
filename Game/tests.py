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

p.capture(Charmander, 'object_forest', b)


capture_explaination(p)


