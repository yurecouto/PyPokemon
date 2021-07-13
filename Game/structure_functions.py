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


def explaination_1(p1):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{f"Your Initial Pokemon was added to the Your pokedex":^98}|')    
    print(f'|{"Pokedex is a python dictionary. ":^98}|')    
    print(f'|{"which receives important information about your pokemons.":^98}|')    
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

    print(f'| Health...................{health_bar(p_1)}||'
          f' Health...................{health_bar(p_2):}|')

    print(f'| XP.......................{xp_bar(p_1)}||'
          f' XP.......................{xp_bar(p_2)}|')

    print('*' * 100)
    print()


def action_status(action):
    print()
    print('*' * 100)
    print(' ', ' ' * 96, ' ')
    print(f' >>> {action:<100}')
    print(' ', ' ' * 96, ' ')
    print('*' * 100)
    print()


def health_bar(pokemon):

    health_dashes = 20  # Max Displayed dashes

    dash_convert = int(pokemon.max_health/health_dashes)            # Get the number to divide by to convert health to dashes (being 10)
    current_dashes = int(pokemon.health/dash_convert)               # Convert health to dash count: 80/10 => 8 dashes
    remaining_health = health_dashes - current_dashes               # Get the health remaining to fill as space => 12 spaces

    health_display = '\033[1;92m#\033[m' * current_dashes           # Convert 8 to 8 dashes as a string:   "--------"
    remaining_display = '-' * remaining_health                      # Convert 12 to 12 spaces as a string: "            "

    return "(" + health_display + remaining_display + ")"           # Print out textbased healthbar


def xp_bar(pokemon):

    xp_dashes = 20  # Max Displayed dashes

    dash_convert = int(pokemon.max_xp/xp_dashes)                    # Get the number to divide by to convert health to dashes (being 10)
    current_dashes = int(pokemon.xp/dash_convert)                   # Convert health to dash count: 80/10 => 8 dashes
    remaining_xp = xp_dashes - current_dashes                       # Get the health remaining to fill as space => 12 spaces

    health_display = '\033[1;34m*\033[m' * current_dashes           # Convert 8 to 8 dashes as a string:   "--------"
    remaining_display = '-' * remaining_xp                          # Convert 12 to 12 spaces as a string: "            "

    return "(" + health_display + remaining_display + ")"           # Print out textbased healthbar
