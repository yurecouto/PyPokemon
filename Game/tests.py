from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random                 import choice, sample

for p in object_forest:
    add(p)

# Where p = pokemon
# And i = info

p1 = Charizard

pokedex_explaination()

for p in v_pokedex:
    print(p)