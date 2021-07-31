from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random import choice

p = Player('Yure')

if p.potions > 0 and p.greatballs > 0 and p.ultraballs > 0 and p.masterballs > 0:
    print('ok')

else:
    print('test')