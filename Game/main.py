from random import choice, randint
from classes import *
from game_functions import *
from structure_functions import *
from pokedex import pokedex
from pokemons import *
                                                          
while True:
    title()                                                 # Title function box
    main_menu()                                             # Main menu function box

    game_mode = int(input('>>> '))

    while game_mode == 1:                                                       # >>> Do some tratative in typing errors <<<
        history_box()
        player_name = input('>>> ')
        player = Player(player_name)

        initial_menu(Bulbasaur, Charmander, Squirtle)
        initial_pokemon = input('>>> ')

        while initial_pokemon.upper() in 'BULBASAUR CHARMANDER SQUIRTLE':       # >>> Do some tratative in typing errors <<<
            if initial_pokemon.upper() == 'CHARMANDER':
                p1 = Charmander
            elif initial_pokemon.upper() == 'BULBASAUR':
                p1 = Bulbasaur
            elif initial_pokemon.upper() == 'SQUIRTLE':
                p1 = Squirtle

            add(p1)
            p1.xp += 55
            p1.level_up()  

            p1.xp += 80
            p1.level_up()   

            p1.xp += 120
            p1.level_up()

            explaination_1()
            player.pokeballs = 20

            area_0 = len(object_forest)
            area_1 = len(object_forest)
            area_2 = len(object_forest)
            area_3 = len(object_forest)
            area_4 = len(object_forest)
            area_5 = len(object_forest)
            area_6 = len(object_forest)
            area_7 = len(object_forest)
            area_8 = len(object_forest)
            area_9 = len(object_forest)

            while area_0 > 0:
                area_explaination('The objects forest')
                p2 = choice(object_forest)

                while True:
                    game_interface(p1)
                    main_interface(p1, p2)

                    action = int(input('>>> '))

                    if action == 1:
                        p1.atack(p2)
                        action_status(f'{p1.name} Atacked {p2.name}')            

                    elif action == 2:
                        player.capture(p2)

                    elif action == 3:
                        pass
                        
                    p2.atack(p1)
                    action_status(f'{p2.name} Atacked {p1.name}')

                    if p2.health <= 0:
                        p1.get_xp(p2)
                        break

                area_0 -= 1        
                    
                