from structure_functions import error_message
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
    pokedex[pokemon] = {
        'number'    : pokemon.number, 
        'type'      : pokemon.type, 
        'level'     : pokemon.lvl, 
        'xp'        : pokemon.xp, 
        'max_hp'    : pokemon.max_health, 
        'hp'        : pokemon.health
        }

# This function sets a level to the initial pokemon
def initial_level(p_object, lvl):
    p_object.lvl         = lvl
    p_object.max_health  = evolution[lvl][1]
    p_object.health      = evolution[lvl][1]
    p_object.max_xp      = evolution[lvl][0]

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

# Use the function pokedex check to use the numbers on the input, it will return the pokemons
# 'selection_fill(pokedex_check(107), pokedex_check(7), pokedex_check(17), pokedex_check(10), pokedex_check(70), pokedex_check(71))'
def selection_fill(p_1, p_2, p_3, p_4, p_5, p_6):
    if p_1 in pokedex:
        selection[0][p_1] = {                           
            'number': p_1.number, 'type': p_1.type, 'level': p_1.lvl, 'xp': p_1.xp, 'max_hp': p_1.max_health, 'hp': p_1.health
                }

    if p_2 in pokedex:
        selection[1][p_2] = {
            'number': p_2.number, 'type': p_2.type, 'level': p_2.lvl, 'xp': p_2.xp, 'max_hp': p_2.max_health, 'hp': p_2.health
                }

    if p_3 in pokedex:
        selection[2][p_3] = {                           
            'number': p_3.number, 'type': p_3.type, 'level': p_3.lvl, 'xp': p_3.xp, 'max_hp': p_3.max_health, 'hp': p_3.health
                }

    if p_4 in pokedex: 
        selection[3][p_4] = {                           
            'number': p_4.number, 'type': p_4.type, 'level': p_4.lvl, 'xp': p_4.xp, 'max_hp': p_4.max_health, 'hp': p_4.health
                }

    if p_5 in pokedex:
        selection[4][p_5] = {                           
            'number': p_5.number, 'type': p_5.type, 'level': p_5.lvl, 'xp': p_5.xp, 'max_hp': p_5.max_health, 'hp': p_5.health
                }

    if p_6 in pokedex:  
        selection[5][p_6] = {                           
            'number': p_6.number, 'type': p_6.type, 'level': p_6.lvl, 'xp': p_6.xp, 'max_hp': p_6.max_health, 'hp': p_6.health
                }

    else:
        error_message('This pokemon is not at the pokedex')
    
# Use the function pokedex check to use the numbers on the input, it will return the pokemons
# 'selection_change(pokedex_check(107), pokedex_check(151))'
def selection_update(p_object_in, p_object_out):
    for n in range(0, 6):
        for k, v in selection[n].items():
            if p_object_out == k:
                k == p_object_in
                selection[n][k] = {
                            'number'    : p_object_in.number, 
                            'type'      : p_object_in.type, 
                            'level'     : p_object_in.lvl, 
                            'xp'        : p_object_in.xp, 
                            'max_hp'    : p_object_in.max_health, 
                            'hp'        : p_object_in.health
        
                         }

# An equivalent to the pokedex_check
def selection_check(p_number):
    for d in selection:
        for pokemon, info in d.items():
            if info['number'] == p_number:
                return True
        
        return False

# An equivalent to the pokemon_change
def selection_change(p_number):
    for d in selection:
        for pokemon, info in d.items():
            if info['number'] == p_number:
                return pokemon
            
