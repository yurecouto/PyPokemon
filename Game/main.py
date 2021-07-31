from random                 import choice, randint
from time                   import sleep
from classes                import *
from game_functions         import *
from structure_functions    import *
from pokemons               import *
                                                          
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
            if initial_pokemon.upper()   == 'CHARMANDER':
                p1 = Charmander
            elif initial_pokemon.upper() == 'BULBASAUR':
                p1 = Bulbasaur
            elif initial_pokemon.upper() == 'SQUIRTLE':
                p1 = Squirtle

            add(p1)

            while True:

                explaination_1()
                player.pokeballs = 10
                player.potions   = 3

                area_0 = len(object_forest)
                area_1 = len(object_mount)
                area_2 = len(object_cave)
                area_3 = len(object_tunnel)
                area_4 = len(object_safari)
                area_5 = len(object_islands)
                area_6 = len(object_road)
                area_7 = len(object_trees)
                area_8 = len(object_valley)
                area_9 = len(object_center)

                area_explaination('The Objects Forest')
                # 3, 7

                while area_0 > 0:
                    pokedex_info_update(p1)
                    p1.level_up()


                    p2 = choice(object_forest)
                    p2.set_level(3, 7)

                    while p2.health > 0: 
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if pokedex_health_check() == False:
                            break

                        if p1.pokemon_out() == False:
                            pokedex_cards()
                            pokedex_explaination('\033[1;101mIn ONLY this area, you can use Pokemons directly from Pokedex\033[m')

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)


                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.pokeballs == 0 and player.greatballs == 0  and player.ultraballs == 0 and player.masterballs == 0 :
                                capture_status(p2, player, 3)
                                break
                                
                            print()
                            capture_explaination(player)

                            print()
                            ball = str(input('>>> '))
                            print()

                            if player.capture(p2, 'object_forest', ball) == True:
                                capture_status(p2, player, 1)
                                break

                            else:
                                capture_status(p2, player, 2)

                        elif action == 3:
                            pokedex_cards()
                            pokedex_explaination('\033[1;101mIn ONLY this area, you can use Pokemons directly from Pokedex\033[m')

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            bag(player)

                            

                            print()
                            item = str(input('>>> '))
                            print()

                            p1.use_potions(player, item)

                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                if pokedex_health_check() == False:
                    break

                pokedex_cards()

                selection_menu("Now, you will select your 6 pokemons, they will compose your selection!")

                p_1 = int(input('>>> '))
                p_2 = int(input('>>> '))
                p_3 = int(input('>>> '))
                p_4 = int(input('>>> '))
                p_5 = int(input('>>> '))
                p_6 = int(input('>>> '))

                selection_fill(
                    pokemon_change(p_1), 
                    pokemon_change(p_2), 
                    pokemon_change(p_3), 
                    pokemon_change(p_4), 
                    pokemon_change(p_5), 
                    pokemon_change(p_6)
                    )

                selection_cards()

                area_explaination('The Objects Mount')
                # 5, 15


                break

            break

        break

    break
  
game_over()  
           