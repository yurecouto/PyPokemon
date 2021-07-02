def title():
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(
          '|\033[1;91m                                                   ▄▄▄                                            \033[m|\n'
          '|\033[1;91m                                                ▄█▀▀▀                                             \033[m|\n'
          '|\033[1;91m                                                                                                  \033[m|\n'
          '|\033[1;91m                      ▄████▄               ▄▄     ▄▄     ▄█  █▄                                   \033[m|\n'
          '|\033[1;91m                  ▄███████████       ▄██  ▄███ ▄██████  ███  ██▄        ███                       \033[m|\n'
          '|\033[1;91m                  ██████▄  ████      ██████▀  ██    ██  ███ ████    ▄▄   ███  ███                 \033[m|\n'
          '|\033[1;91m                    ▀████   ██▀ ▄██▄  ▀████   ███  ▀▀   ████████  ██████ ███  ██▀                 \033[m|\n'
          '|\033[1;91m                     ▀███▄ ▄█▀ ██████  ██████  ███▄▄▄▄█ ██ ██▀▀█ ██    ██ ██████                  \033[m|\n'
          '|\033[1;91m                      ▀█████▀ ███  ███ ██  ███▄  ▀███▀ ██  █▀  █ ██▄  ▄█ ██████▀                  \033[m|\n'
          '|\033[1;91m                       ▀███▀   ██████  ██    ▀███▄              ▀ █████ ██  ███                   \033[m|\n'
          '|\033[1;91m                        ▀███▄   ▀██▀   ██       ▀▀                  ▀▀ ██   ██▀                   \033[m|\n'
          '|\033[1;91m                         ▀███           ▀                                   ██                    \033[m|\n'
          '|\033[1;91m                          ▀██▄              AN OOP ADVENTURE!               █▀                    \033[m|'
          )
    print('|', ' ' * 96, '|')
    print('*' * 100)


def main_menu():
    new_game = '\033[1;34mNEW GAME\033[m'
    continue_game = '\033[1;92mCONTINUE\033[m'
    game_credits = '\033[1;93mCREDITS\033[m'

    print('|', ' ' * 96, '|')
    print(f"|{f'Press 1 for {new_game} | 2 to try to {continue_game} | 3 to see your {game_credits}':^128}|")
    print('|', ' ' * 96, '|')
    print('*' * 100)


def initial_menu(ip_1, ip_2, ip_3, ip_4):
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"Choose your initial Pokemon!":^98}|')
    print('|', ' ' * 96, '|')
    print(f'|{f"{ip_1} | {ip_2} | {ip_3} | {ip_4}":^138}|')
    print('|', ' ' * 96, '|')
    print('*' * 100)


def main_interface(p_1, p_2):
    print('-' * 100)
    print(f'|{p_1.name:^58}||{p_2.name:^58}|')
    print('-' * 100)

    print(f'|{"Status":^48}||{"Status":^48}|')

    print(f'| Health...................{health_bar(p_1.max_health, p_1.health)}||'
          f' Health...................{health_bar(p_2.max_health, p_2.health):}|')

    print(f'| XP.......................{xp_bar(p_1.xp, 100)}||'
          f' XP.......................{xp_bar(p_2.xp, 100)}|')

    print('*' * 100)


def game_interface(my_pokemon):
    atack = '\033[1;91mATACK\033[m'
    capture = '\033[1;92mCAPTURE\033[m'
    bag = '\033[1;93mBAG\033[m'

    print('*' * 100)
    print(f'|{"Options":^98}|')
    print('-' * 100)

    print(f"|{f'My Pokemon: {my_pokemon.name}!':^108}|")

    print(f'|{" " * 98}|')
    print(f"|{f'Press 1 for {atack} | 2 to try to {capture} | 3 to see your {bag}':^128}|")


def action_status(action):
    print('*' * 100)
    print(' ', ' ' * 96, ' ')
    print(f' >>> {action:<100}' + ' ')
    print(' ', ' ' * 96, ' ')
    print('*' * 100)


def health_bar(max_health, health):

    health_dashes = 20  # Max Displayed dashes

    dash_convert = int(max_health/health_dashes)                 # Get the number to divide by to convert health to dashes (being 10)
    current_dashes = int(health/dash_convert)                     # Convert health to dash count: 80/10 => 8 dashes
    remaining_health = health_dashes - current_dashes             # Get the health remaining to fill as space => 12 spaces

    health_display = '\033[1;92m#\033[m' * current_dashes         # Convert 8 to 8 dashes as a string:   "--------"
    remaining_display = '-' * remaining_health                    # Convert 12 to 12 spaces as a string: "            "

    return "(" + health_display + remaining_display + ")"    # Print out textbased healthbar


def xp_bar(xp, max_xp):

    xp_dashes = 20  # Max Displayed dashes

    dash_convert = int(max_xp/xp_dashes)                 # Get the number to divide by to convert health to dashes (being 10)
    current_dashes = int(xp/dash_convert)                     # Convert health to dash count: 80/10 => 8 dashes
    remaining_xp = xp_dashes - current_dashes             # Get the health remaining to fill as space => 12 spaces

    health_display = '\033[1;34m*\033[m' * current_dashes         # Convert 8 to 8 dashes as a string:   "--------"
    remaining_display = '-' * remaining_xp                   # Convert 12 to 12 spaces as a string: "            "

    return "(" + health_display + remaining_display + ")" # Print out textbased healthbar



