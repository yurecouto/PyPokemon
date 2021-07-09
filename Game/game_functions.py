from random import randint
from pokedex import *

def damage(base, intensity):
    min_d = int(5  * intensity)
    max_d = int(25 * intensity)
    atack = randint((int((base * min_d) / 100)), int((base * max_d) / 100))
    return atack

def capture(pokemon):
    probability = randint(0, 100)

    if probability <= 33:
        pokedex[pokemon.name] = [pokemon.type, pokemon.lvl, pokemon.xp]
        print(pokemon.name, 'Was Captured')
    
    else:
        print(pokemon.name, 'Was not Captured')

    