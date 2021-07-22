from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random import choice


add(Meowth)
add(Squirtle)
add(Bulbasaur)
add(Nidoking)
add(Charmander)
add(Mew)

p1 = Charizard
print(p1.name)

n = int(input('>>> '))

if pokedex_check(n) == True:
    p1 = pokemon_change(n)

print(p1.name)
