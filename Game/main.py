from game_functions import capture
from classes import *
from structure_functions import *
from pokedex import pokedex
from pokemons import *
                                                            
while True:
    title()                                                 # Title function box
    main_menu()                                             # Main menu function box

    game_mode = int(input('>>> '))

    while game_mode == 1:                                                   # >>> Do some tratative in typing errors <<<
        history_box()
        initial_menu(Bulbasaur, Charmander, Squirtle)

        initial_pokemon = input('>>> ')

        while initial_pokemon.upper in 'BULBASAUR CHARMANDER SQUIRTLE':     # >>> Do some tratative in typing errors <<<
            
            if initial_pokemon.upper == 'CHARMANDER':
                p1 = Charmander
            elif initial_pokemon.upper == 'BULBASAUR':
                p1 = Bulbasaur
            elif initial_pokemon.upper == 'SQUIRTLE':
                p1 = Squirtle

            capture()