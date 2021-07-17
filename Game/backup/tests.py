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


pokedex_explaination()

choice = int(input('>>> '))

if choice == pokedex[Abra]['number']:
    p1 = Abra

for p in pokedex:
    print(p)

print(Bulbasaur.number)