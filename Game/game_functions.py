from random import randint
from pokedex import *
from lists import evolution

# This function it's responsable for the atack
def damage(base, intensity):
    min_d = int(5  * intensity)
    max_d = int(25 * intensity)
    atack = randint((int((base * min_d) / 100)), int((base * max_d) / 100))
    return atack

# This function adds a pokemon without resistance to the pokedex (a dictionary)   
def add(pokemon):
    pokedex[pokemon.name] = [pokemon.type, pokemon.lvl, pokemon.xp]
    print(pokemon.name, 'Was Added to your Pokedex')

# This function adds a pokemon with resistance to the pokedex (a dictionary)  
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

# This function sets random levels to the pokemons in the areas
def area_level(area, min_l, max_l):
    for pokemon in area:
        lvl = randint(min_l, max_l)
        pokemon.lvl         = lvl
        pokemon.max_health  = evolution[lvl][1]
        pokemon.health      = evolution[lvl][1]
        pokemon.max_xp      = evolution[lvl][0]

# This function sets a level to the initial pokemon
def ip_level(pokemon, lvl):
    pokemon.lvl         = lvl
    pokemon.max_health  = evolution[lvl][1]
    pokemon.health      = evolution[lvl][1]
    pokemon.max_xp      = evolution[lvl][0]
