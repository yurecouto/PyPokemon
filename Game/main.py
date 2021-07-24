from random                 import choice, randint
from classes                import *
from game_functions         import *
from structure_functions    import *
from pokedex                import pokedex
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
                player.pokeballs = 20

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
                    p2 = choice(object_forest)

                    p2.set_level(3, 7)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            capture_explaination(player)
                            ball = int(input('>>> '))

                            player.capture(p2, 'object_forest', ball)

                            if player.capture(p2, 'object_forest', ball) == True:
                                capture_status()

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Mount')
                # 5, 15

                while area_1 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(5, 15)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Cave')
                # 12, 20

                while area_2 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(12, 20)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Tunnel')
                # 16, 24

                while area_3 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(16, 24)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Safari')
                # 22, 32

                while area_4 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(22, 32)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Islands')
                # 28, 42

                while area_5 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(28, 42)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Road')
                # 38, 56

                while area_6 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(38, 56)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Trees')
                # 50, 62

                while area_7 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(50, 62)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Valley')
                # 65, 85

                while area_8 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(65, 85)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                area_explaination('The Objects Center')
                # 90, 99

                while area_9 > 0:
                    p2 = choice(object_forest)

                    p2.set_level(90, 99)

                    while p2.health > 0:
                        pokedex_health_check()    
                        if pokedex_health_check() == False:
                            break

                        pokedex_info_update(p1)
                        p1.level_up()
                        main_interface(p1, p2)

                        action = int(input('>>> '))

                        if action == 1:
                            p1.atack(p2)
                            action_status(f'{p1.name} Atacked {p2.name}')            

                        elif action == 2:
                            if player.capture(p2) == True:
                                break

                        elif action == 3:
                            my_pokedex()
                            pokedex_explaination()

                            p_number = int(input('>>> '))

                            if pokedex_check(p_number) == True:
                                p1 = pokemon_change(p_number)
                                
                        elif action == 4:
                            pass
                    
                        p2.atack(p1)
                        action_status(f'{p2.name} Atacked {p1.name}')

                    xp = int(p2.max_xp / 7)
                    p1.xp += xp
                    area_0 -= 1  

                    if pokedex_health_check() == False:
                        break

                break

            break

        break

    break
  
game_over()  
           