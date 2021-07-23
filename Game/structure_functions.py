from pokedex import pokedex

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


def pokedex_explaination():
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"This is your pokedex":^98}|')    
    print(f'|{"Type the correct Number of the pokemon you wanna use":^98}|')    
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def initial_menu(ip1, ip2, ip3):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"Choose your initial Pokemon!":^98}|')
    print('|', ' ' * 96, '|')
    print(f'|{f"{ip1.name} | {ip2.name} | {ip3.name}":^128}|')
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def main_interface(p1, p2):
    print()
    atack   = '\033[1;91mATACK\033[m'
    capture = '\033[1;92mCAPTURE\033[m'
    change  = '\033[1;94mCHANGE POKEMON\033[m'
    bag     = '\033[1;93mBAG\033[m'

    print('*' * 100)
    print(f'|{"Options":^98}|')
    print('+' + '-' * 98 + '+')

    print(f"|{f'My Pokemon: {p1.name}!':^108}|")

    print(f'|{" " * 98}|')
    print(f"|{f'Press 1 for {atack} | 2 to try to {capture} || 3 to {change} | 4 to see your {bag}':^138}|")

    print('+' + '-' * 98 + '+')
    print(f'|{p1.name:^58}||{p2.name:^58}|')
    print('+' + '-' * 98 + '+')

    print(f'|{"Status":^48}||{"Status":^48}|')

    print(f'| Health...................{hp_bar(p1)}||'
          f' Health...................{hp_bar(p2)}|')

    print(f'| XP.......................{xp_bar(p1)}||'
          f' XP.......................{xp_bar(p2)}|')

    print(f'| Level....................................(#{p1.lvl:^3})||'
          f' Level....................................(#{p2.lvl:^3})|')

    print('*' * 100)
    print()


def action_status(action):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print('|', f'{action:^116}', '|')
    print('|', ' ' * 96, '|')
    print('*' * 100)
    print()


def hp_bar(p):
    hp_dashes = int((p.health * 20) / p.max_health)
    hp_remaining = 20 - hp_dashes

    if hp_dashes <= 20 and hp_dashes >= 13:
        return '(' + '\033[1;92m#\033[m' * hp_dashes + '-' * hp_remaining + ')'

    elif hp_dashes < 13 and hp_dashes >= 6:
        return '(' + '\033[1;93m#\033[m' * hp_dashes + '-' * hp_remaining + ')'

    elif hp_dashes < 6 and hp_dashes >= 0:
        return '(' + '\033[1;91m#\033[m' * hp_dashes + '\033[1;91m-\033[m' * hp_remaining + ')'


def xp_bar(p):
    l = p.max_xp - p.xp
    xp_dashes = int((l * 20) / p.max_xp)
    xp_remaining = 20 - xp_dashes

    return '(' + '\033[1;94m#\033[m' * xp_remaining + '\033[1;94m-\033[m' * xp_dashes + ')'


def game_over():
    print('                                                                ')
    print('             /██████                                            ')
    print('            /██__  ██                                           ')
    print('           | ██  \__/  /██████  /██████/████   /██████          ')
    print('           | ██ /████ |____  ██| ██_  ██_  ██ /██__  ██         ')
    print('           | ██|_  ██  /███████| ██ \ ██ \ ██| ████████         ')
    print('           | ██  \ ██ /██__  ██| ██ | ██ | ██| ██_____/         ')
    print('           |  ██████/|  ███████| ██ | ██ | ██|  ████████        ')
    print('            \______/  \_______/|__/ |__/ |__/ \_______/         ')
    print('                                                                ')
    print('             /██████  /██    /██ /██████   /██████              ')
    print('            /██__  ██|  ██  /██//██__  ██ /██__  ██             ')
    print('           | ██  \ ██ \  ██/██/| ████████| ██  \__/             ')
    print('           | ██  | ██  \  ███/ | ██_____/| ██                   ')
    print('           |  ██████/   \  █/  |  ███████| ██                   ')
    print('            \______/     \_/    \_______/|__/                   ')
    print('                                                                ')


def my_pokedex():
    for p, i in pokedex.items():
        print('-------------------') 
        print(f'|{p.name:^27}|')
        print('-------------------') 

        for keys, values in i.items():
            print(f'|{keys:<6}: {values:>9}|')

        print('-------------------')


