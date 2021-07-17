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
    pokedex[pokemon] = {'number' : pokemon.number, 'type' : pokemon.type, 'level' : pokemon.lvl, 'xp' : pokemon.xp, 'hp': pokemon.max_health}
    print(pokemon.name, 'Was Added to your Pokedex')

# This function sets random levels to the pokemons in the areas
def area_level(area, min_l, max_l):
    for pokemon in area:
        lvl = randint(min_l, max_l)
        pokemon.lvl         = lvl
        pokemon.max_health  = evolution[lvl][1]
        pokemon.health      = evolution[lvl][1]
        pokemon.max_xp      = evolution[lvl][0]

# This function sets random levels to a single pokemon
def p_level(pokemon, min_l, max_l):
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
