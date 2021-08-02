from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random import choice
from time import sleep

add(Bulbasaur)
add(Charmander)
add(Squirtle)
add(Pikachu)
add(Eevee)
add(Nidorano)

p1 = Charizard
print(p1.name)

selection_fill(Bulbasaur, Charmander, Squirtle, Pikachu, Eevee, Nidorano)

p1 = selection_change(6)
print(p1.name)
