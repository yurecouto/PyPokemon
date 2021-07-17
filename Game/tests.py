from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *

p1 = Charmander
print(p1.name)

add(Abra)
add(Bulbasaur)

number = int(input('>>> '))

# testar essas duas funcções como uma, caso não funcione
# mover para o arquivo game_functions

def pokedex_check(p_number):
    for pokemon, info in pokedex.items():
        for key, value in info.items():
            if key == 'number' and value == p_number:
                return 'yes'

            else:
                return 'no'

def pokemon_change(p_number):
    for pokemon, info in pokedex.items():
        for key, value in info.items():
            if key == 'number' and value == p_number:
                return pokemon

pokedex_check(number)
if pokedex_check(number) == 'yes':
    p1 = pokemon_change(number)

print(p1.name)
