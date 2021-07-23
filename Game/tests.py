from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random import choice

add(Charmander)
add(Pikachu)
add(Eevee)
add(Venusaur)

my_pokedex()

Squirtle.atack(Charmander)
print(Charmander.health)
pokedex_info_update(Charmander)
my_pokedex()