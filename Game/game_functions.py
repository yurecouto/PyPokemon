from random import randint
from pokedex import *
from lists import evolution

def damage(base, intensity):
    min_d = int(5  * intensity)
    max_d = int(25 * intensity)
    atack = randint((int((base * min_d) / 100)), int((base * max_d) / 100))
    return atack
    
def add(pokemon):
    pokedex[pokemon.name] = [pokemon.type, pokemon.lvl, pokemon.xp]
    print(pokemon.name, 'Was Added to your Pokedex')

def capture(player, pokemon):
    if player.pokeballs > 0:

        probability = randint(0, 100)
        player.pokeballs -= 1

        if probability <= 33:
            pokedex[pokemon.name] = [pokemon.type, pokemon.lvl, pokemon.xp]
            print(pokemon.name, 'Was Captured', f'{player.pokeballs} pokeballs remaining')
        
        else:
            print(pokemon.name, 'Was not Captured', f'{player.pokeballs} pokeballs remaining')

    else:
        print(f"{player.name}, you don't have enough Pokeballs")

def area_level(area, min_l, max_l):
    for pokemon in area:
        lvl = randint(min_l, max_l)
        pokemon.lvl         = lvl
        pokemon.max_health  = evolution[lvl][1]
        pokemon.health      = evolution[lvl][1]
        pokemon.max_xp      = evolution[lvl][0]


