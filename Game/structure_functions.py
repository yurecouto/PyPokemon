from time import perf_counter


def title():
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(
          '|\033[1;91m                                                   ▄▄▄                                            \033[m|\n'
          '|\033[1;91m                                                ▄█▀▀▀                                             \033[m|\n'
          '|\033[1;91m                                                                                                  \033[m|\n'
          '|\033[1;91m                      ▄████▄               ▄▄     ▄▄▄    ▄█  █▄                                   \033[m|\n'
          '|\033[1;91m                  ▄███████████       ▄██  ▄███ ▄██████  ███  ██▄        ███                       \033[m|\n'
          '|\033[1;91m                  ██████▄  ████      ██████▀  ██    ██  ███ ████    ▄▄   ███  ███                 \033[m|\n'
          '|\033[1;91m                    ▀████   ██▀ ▄██▄  ▀████   ███  ▀▀   ████████  ██████ ███  ██▀                 \033[m|\n'
          '|\033[1;91m                     ▀███▄ ▄█▀ ██████  ██████  ███▄▄▄▄█ ██ ██▀▀█ ██▀  ▀██ ██████                  \033[m|\n'
          '|\033[1;91m                      ▀█████▀ ███  ███ ██  ███▄  ▀███▀ ██  █▀  █ ██▄  ▄█ ██████▀                  \033[m|\n'
          '|\033[1;91m                       ▀███▀   ██████  ██    ▀███▄              ▀ █████ ██  ███                   \033[m|\n'
          '|\033[1;91m                        ▀███▄   ▀██▀   ██       ▀▀                  ▀▀ ██   ██▀                   \033[m|\n'
          '|\033[1;91m                         ▀███           ▀                                   ██                    \033[m|\n'
          '|\033[1;91m                          ▀██▄              AN OOP ADVENTURE!               █▀                    \033[m|'
          )
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def main_menu():
    print('*' * 100)
    new_game = '\033[1;34mNEW GAME\033[m'
    continue_game = '\033[1;92mCONTINUE\033[m'
    game_credits = '\033[1;93mCREDITS\033[m'

    print('|', ' ' * 96, '|')
    print(f"|{f'Press 1 for {new_game} | 2 to try to {continue_game} | 3 to see your {game_credits}':^128}|")
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def history_box():
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"This Game is an adventure in Python OOP World":^98}|')    
    print(f'|{"In this world the Objects started to take the shape of the Pokemons":^98}|')    
    print(f'|{"Your mission is to defeat or capture all the objects, good luck!":^98}|')    
    print('|', ' ' * 96, '|')
    print(f'|{"Type your name in the input bellow:":^98}|')   
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def explaination_1():
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"Your Initial Pokemon was added to the Your pokedex":^98}|')    
    print(f'|{"Pokedex is a python dictionary. ":^98}|')    
    print(f'|{"which receives important information about your pokemons.":^98}|')    
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def area_explaination(area):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{area:^98}|')    
    print(f'|{"Now the game starts, Clear that area!":^98}|')    
    print(f'|{"You can do this by Capturing the pokemons or beating them!":^98}|')    
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def initial_menu(ip_1, ip_2, ip_3):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"Choose your initial Pokemon!":^98}|')
    print('|', ' ' * 96, '|')
    print(f'|{f"{ip_1.name} | {ip_2.name} | {ip_3.name}":^128}|')
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def game_interface(my_pokemon):
    print()
    atack = '\033[1;91mATACK\033[m'
    capture = '\033[1;92mCAPTURE\033[m'
    bag = '\033[1;93mBAG\033[m'

    print('*' * 100)
    print(f'|{"Options":^98}|')
    print('-' * 100)

    print(f"|{f'My Pokemon: {my_pokemon.name}!':^108}|")

    print(f'|{" " * 98}|')
    print(f"|{f'Press 1 for {atack} | 2 to try to {capture} | 3 to see your {bag}':^128}|")


def main_interface(p_1, p_2):
    print('-' * 100)
    print(f'|{p_1.name:^58}||{p_2.name:^58}|')
    print('-' * 100)

    print(f'|{"Status":^48}||{"Status":^48}|')

    print(f'| Health...................{hp_bar(p_1)}||'
          f' Health...................{hp_bar(p_2)}|')

    print(f'| XP.......................{xp_bar(p_1)}||'
          f' XP.......................{xp_bar(p_2)}|')

    print('*' * 100)
    print()


def action_status(action):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print('|', f'{action:^98}', '|')
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def hp_bar(p):
    if p.health > 0:
        if p.health == p.max_health:
            return '(' + '\033[1;92m#\033[m' * 20 + ')'

        elif p.health < p.max_health and p.health >= (p.max_health * 95 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 19 + '-)'

        elif p.health < (p.max_health * 95 ) / 100 and p.health >= (p.max_health * 90 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 18 + '-' * 2 + ')'

        elif p.health < (p.max_health * 90 ) / 100 and p.health >= (p.max_health * 85 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 17 + '-' * 3 + ')'

        elif p.health < (p.max_health * 85 ) / 100 and p.health >= (p.max_health * 80 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 16 + '-' * 4 + ')'

        elif p.health < (p.max_health * 80 ) / 100 and p.health >= (p.max_health * 75 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 15 + '-' * 5 + ')'

        elif p.health < (p.max_health * 75 ) / 100 and p.health >= (p.max_health * 70 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 14 + '-' * 6 + ')'

        elif p.health < (p.max_health * 70 ) / 100 and p.health >= (p.max_health * 65 ) / 100:
            return '(' + '\033[1;92m#\033[m' * 13 + '-' * 7 + ')'
            
        elif p.health < (p.max_health * 65 ) / 100 and p.health >= (p.max_health * 60 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 12 + '-' * 8 + ')'

        elif p.health < (p.max_health * 60 ) / 100 and p.health >= (p.max_health * 55 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 11 + '-' * 9 + ')'

        elif p.health < (p.max_health * 55 ) / 100 and p.health >= (p.max_health * 50 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 10 + '-' * 10 + ')'
    
        elif p.health < (p.max_health * 50 ) / 100 and p.health >= (p.max_health * 45 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 9 + '-' * 11 + ')'
    
        elif p.health < (p.max_health * 45 ) / 100 and p.health >= (p.max_health * 40 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 8 + '-' * 12 + ')'
    
        elif p.health < (p.max_health * 40 ) / 100 and p.health >= (p.max_health * 35 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 7 + '-' * 13 + ')'
    
        elif p.health < (p.max_health * 35 ) / 100 and p.health >= (p.max_health * 30 ) / 100:
            return '(' + '\033[1;93m#\033[m' * 6 + '-' * 14 + ')'
    
        elif p.health < (p.max_health * 30 ) / 100 and p.health >= (p.max_health * 25 ) / 100:
            return '(' + '\033[1;91m#\033[m' * 5 + '-' * 15 + ')'
    
        elif p.health < (p.max_health * 25 ) / 100 and p.health >= (p.max_health * 20 ) / 100:
            return '(' + '\033[1;91m#\033[m' * 4 + '-' * 16 + ')'
    
        elif p.health < (p.max_health * 20 ) / 100 and p.health >= (p.max_health * 15 ) / 100:
            return '(' + '\033[1;91m#\033[m' * 3 + '-' * 17 + ')'
    
        elif p.health < (p.max_health * 15 ) / 100 and p.health >= (p.max_health * 10 ) / 100:
            return '(' + '\033[1;91m#\033[m' * 2 + '-' * 18 + ')'
    
        elif p.health < (p.max_health * 10 ) / 100 and p.health >= (p.max_health * 5 ) / 100:
            return '(' + '\033[1;91m#\033[m' * 1 + '-' * 19 + ')'
    
        elif p.health < (p.max_health * 5 ) / 100 and p.health > (p.max_health * 0 ) / 100:
            return '(' + '\033[1;91m#\033[m' * 1 + '-' * 20 + ')'
    
    else:
        return '(' + '\033[1;91m-\033[m' * 20 +')'


def xp_bar(p):
    if p.xp > 0:
        if p.xp == p.max_xp:
            return '(' + '\033[1;94m#\033[m' * 20 + ')'

        elif p.xp < p.max_xp and p.xp >= (p.max_xp * 95 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 19 + '-)'

        elif p.xp < (p.max_xp * 95 ) / 100 and p.xp >= (p.max_xp * 90 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 18 + '-' * 2 + ')'

        elif p.xp < (p.max_xp * 90 ) / 100 and p.xp >= (p.max_xp * 85 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 17 + '-' * 3 + ')'

        elif p.xp < (p.max_xp * 85 ) / 100 and p.xp >= (p.max_xp * 80 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 16 + '-' * 4 + ')'

        elif p.xp < (p.max_xp * 80 ) / 100 and p.xp >= (p.max_xp * 75 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 15 + '-' * 5 + ')'

        elif p.xp < (p.max_xp * 75 ) / 100 and p.xp >= (p.max_xp * 70 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 14 + '-' * 6 + ')'

        elif p.xp < (p.max_xp * 70 ) / 100 and p.xp >= (p.max_xp * 65 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 13 + '-' * 7 + ')'
            
        elif p.xp < (p.max_xp * 65 ) / 100 and p.xp >= (p.max_xp * 60 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 12 + '-' * 8 + ')'

        elif p.xp < (p.max_xp * 60 ) / 100 and p.xp >= (p.max_xp * 55 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 11 + '-' * 9 + ')'

        elif p.xp < (p.max_xp * 55 ) / 100 and p.xp >= (p.max_xp * 50 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 10 + '-' * 10 + ')'
    
        elif p.xp < (p.max_xp * 50 ) / 100 and p.xp >= (p.max_xp * 45 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 9 + '-' * 11 + ')'
    
        elif p.xp < (p.max_xp * 45 ) / 100 and p.xp >= (p.max_xp * 40 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 8 + '-' * 12 + ')'

        elif p.xp < (p.max_xp * 40 ) / 100 and p.xp >= (p.max_xp * 35 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 7 + '-' * 13 + ')'
    
        elif p.xp < (p.max_xp * 35 ) / 100 and p.xp >= (p.max_xp * 30 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 6 + '-' * 14 + ')'
    
        elif p.xp < (p.max_xp * 30 ) / 100 and p.xp >= (p.max_xp * 25 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 5 + '-' * 15 + ')'
    
        elif p.xp < (p.max_xp * 25 ) / 100 and p.xp >= (p.max_xp * 20 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 4 + '-' * 16 + ')'
    
        elif p.xp < (p.max_xp * 20 ) / 100 and p.xp >= (p.max_xp * 15 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 3 + '-' * 17 + ')'
    
        elif p.xp < (p.max_xp * 15 ) / 100 and p.xp >= (p.max_xp * 10 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 2 + '-' * 18 + ')'
    
        elif p.xp < (p.max_xp * 10 ) / 100 and p.xp >= (p.max_xp * 5 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 1 + '-' * 19 + ')'
    
        elif p.xp < (p.max_xp * 5 ) / 100 and p.xp > (p.max_xp * 0 ) / 100:
            return '(' + '\033[1;94m#\033[m' * 1 + '-' * 20 + ')'
    
    else:
        return '(' + '\033[1;94m-\033[m' * 20 +')'

