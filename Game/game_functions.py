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
'''Use pokemon.number as key value'''
def add(pokemon):
    pokedex[pokemon] = {'number' : pokemon.number, 'type' : pokemon.type, 'level' : pokemon.lvl, 'xp' : pokemon.xp, 'hp': pokemon.max_health}
    print(pokemon.name, 'Was Added to your Pokedex')


# This function sets a level to the initial pokemon
def initial_level(pokemon, lvl):
    pokemon.lvl         = lvl
    pokemon.max_health  = evolution[lvl][1]
    pokemon.health      = evolution[lvl][1]
    pokemon.max_xp      = evolution[lvl][0]

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
            print(pokemon.name + 'Found') 
            return pokemon

# Thats the correct way to use the 2 functions above
'''pokedex_check(number)
if pokedex_check(number) == 'yes':
    p1 = pokemon_change(number)'''

