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
def add(pokemon, dictionary):
    if dictionary == selection:
        if len(dictionary) <= 5:
            dictionary[pokemon] = {
                'number'    : pokemon.number, 
                'type'      : pokemon.type, 
                'level'     : pokemon.lvl, 
                'xp'        : pokemon.xp, 
                'max_hp'    : pokemon.max_health, 
                'hp'        : pokemon.health
                }
                
        else:
            print("\033[1;91mYOUR SELECTION IT'S FULL\033[m")
            print("Please, change your selection")

    elif dictionary == pokedex:
        dictionary[pokemon] = {
            'number'    : pokemon.number, 
            'type'      : pokemon.type, 
            'level'     : pokemon.lvl, 
            'xp'        : pokemon.xp, 
            'max_hp'    : pokemon.max_health, 
            'hp'        : pokemon.health
            }


# This function sets a level to the initial pokemon
def initial_level(pokemon, lvl):
    pokemon.lvl         = lvl
    pokemon.max_health  = evolution[lvl][1]
    pokemon.health      = evolution[lvl][1]
    pokemon.max_xp      = evolution[lvl][0]

# This function checks if you have at least one alive pokemon on your pokedex
def pokedex_health_check():
    alive = len(pokedex)

    for pokemon, info in pokedex.items():
        if info['hp'] < 1:
            alive -= 1 

    while alive == 0:
        return False

    else:
        return True

# This function checks if you have the pokemon on your pokedex
def pokedex_check(p_number):
    for pokemon, info in pokedex.items():
        if info['number'] == p_number:
            return True

    return False

# This function returns the pokemon checked
def pokemon_change(p_number):
    for pokemon, info in pokedex.items():
        if info['number'] == p_number:
            return pokemon

# this function updates the pokemon infos into the pokedex
def pokedex_info_update(p_object):
    for pokemon, info in pokedex.items():
        if info['number'] == p_object.number:
            if p_object.health < info['max_hp']:
                pokedex[p_object]['hp']     = p_object.health
                pokedex[p_object]['xp']     = p_object.xp
                pokedex[p_object]['level']  = p_object.lvl
                return pokedex
