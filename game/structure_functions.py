from pokedex import *

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


def received_items(
    item_1 = '', qtd_1 = 0,
    item_2 = '', qtd_2 = 0,
    item_3 = '', qtd_3 = 0,
    item_4 = '', qtd_4 = 0,
    item_5 = '', qtd_5 = 0,
    item_6 = '', qtd_6 = 0,
    txt = 0):

    print('*' * 100)
    print('|' + ' ' * 98 + '|')
    if txt == 0:
        print(f'|{"There are the items you will receive to clear this area:":^98}|') 

    elif txt == 1:
        print(f'|{"For clearing the last area, You will receive this items:":^98}|') 

    print('|' + ' ' * 98 + '|')

    if item_1 != '':
        print(f"|{f'{item_1}      X {qtd_1}':^98}|")

    if item_2 != '':
        print(f"|{f'{item_2}      X {qtd_2}':^98}|")

    if item_3 != '':
        print(f"|{f'{item_3}      X {qtd_3}':^98}|")

    if item_4 != '':
        print(f"|{f'{item_4}      X {qtd_4}':^98}|")

    if item_5 != '':
        print(f"|{f'{item_5}      X {qtd_5}':^98}|")

    if item_6 != '':
        print(f"|{f'{item_6}      X {qtd_6}':^98}|")

    print('|' + ' ' * 98 + '|')
    print('*' * 100)


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


def pokedex_explaination(txt = ''):
    print()
    print('*' * 100)
    print('|', ' ' * 96, '|')
    print(f'|{"This is your pokedex":^98}|') 
    print('|', ' ' * 96, '|')
    print(f'|{txt:^109}|')    
    print('|', ' ' * 96, '|')
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

    elif hp_dashes < 0:
        return '(' + '\033[1;91m-\033[m' * 3 + '\033[1;91mOUT-OF-COMBAT!\033[m' + '\033[1;91m-\033[m' * 3 + ')'


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


def capture_explaination(player):
    pokeballs   = str('\033[1;91mPoke\033[m'  + '\033[1;37mballs\033[m')
    greatballs  = str('\033[1;36mGreat\033[m' + '\033[1;37mballs\033[m')
    ultraballs  = str('\033[1;93mUltra\033[m' + '\033[1;37mballs\033[m')
    masterballs = str('\033[1;95mMaster\033[m'+ '\033[1;37mballs\033[m')

    print('*' * 100)
    print('|' + ' ' * 98 + '|')
    print(f'|{"Choose the pokeball you wanna use to capture":^98}|') 
    print('|' + ' ' * 98 + '|')
    print(f'|{f"1 - {pokeballs}: {player.pokeballs} | 2 - {greatballs}: {player.greatballs} | 3 - {ultraballs}: {player.ultraballs} | 4 - {masterballs}: {player.masterballs}":^178}|')
    print('|', ' ' * 96, '|')
    print('*' * 100)


def capture_status(p2, player, result):
    if result == 1:
        print('*' * 100)
        print('|', ' ' * 96, '|')
        print(f'|{f"{player.name.upper()}, you have captured the wild pokemon:":^98}|') 
        print('|', ' ' * 96, '|')
        print(f'|{p2.name:^108}|') 
        print(f'|{"Now it is in your Pokedex.":^98}|') 
        print('|', ' ' * 96, '|')
        print('*' * 100)
    
    elif result == 2:
        print('*' * 100)
        print('|', ' ' * 96, '|')
        print(f'|{f"{player.name.upper()}, you have NOT captured the wild pokemon:":^98}|') 
        print(f'|{"Try again if you have enought pokeballs!":^98}|') 
        print('|', ' ' * 96, '|')
        print('*' * 100)  

    elif result == 3:
        print('*' * 100)
        print('|', ' ' * 96, '|')
        print(f'|{f"{player.name.upper()}, You do NOT have enought POKEBALLS" :^98}|') 
        print('|', ' ' * 96, '|')
        print('*' * 100)


def pokedex_cards():
    print('-' * 100)
    print (f"| {'Name':^10} | {'Number':^12} | {'Type':^12} | {'Level':^12} | {'XP':^12} | {'Max HP':^10} | {'HP':^10} |")
    print('-' * 100)

    for p, i in pokedex.items():
        print(f"| {p.name:<20} | {i['number']:^12} | {i['type']:^12} | {i['level']:^12} | {i['xp']:^12} | {i['max_hp']:^10} | {i['hp']:^10} |")
        print('-' * 100)


def selection_cards():
    print('-' * 108)

    pokemons_0 = list(selection[0].keys())
    pokemons_1 = list(selection[1].keys())
    pokemons_2 = list(selection[2].keys())
    pokemons_3 = list(selection[3].keys())
    pokemons_4 = list(selection[4].keys())
    pokemons_5 = list(selection[5].keys())

    print(f'| {pokemons_0[0].name:^24} || {pokemons_1[0].name:^24} || {pokemons_2[0].name:^24} || {pokemons_3[0].name:^24} || {pokemons_4[0].name:^24} || {pokemons_5[0].name:^24} |')

    print(('|' + '-' * 16 + '|') * 6)

    print(f'|{"number":<6}:{pokemons_0[0].number:>9}||{"number":<6}:{pokemons_1[0].number:>9}||{"number":<6}:{pokemons_2[0].number:>9}||{"number":<6}:{pokemons_3[0].number:>9}||{"number":<6}:{pokemons_4[0].number:>9}||{"number":<6}:{pokemons_5[0].number:>9}|') 

    print(f'|{"type":<6}:{pokemons_0[0].type:>9}||{"type":<6}:{pokemons_1[0].type:>9}||{"type":<6}:{pokemons_2[0].type:>9}||{"type":<6}:{pokemons_3[0].type:>9}||{"type":<6}:{pokemons_4[0].type:>9}||{"type":<6}:{pokemons_5[0].type:>9}|')

    print(f'|{"health":<6}:{pokemons_0[0].health:>9}||{"health":<6}:{pokemons_1[0].health:>9}||{"health":<6}:{pokemons_2[0].health:>9}||{"health":<6}:{pokemons_3[0].health:>9}||{"health":<6}:{pokemons_4[0].health:>9}||{"health":<6}:{pokemons_5[0].health:>9}|')

    print(f'|{"level":<6}:{pokemons_0[0].lvl:>9}||{"level":<6}:{pokemons_1[0].lvl:>9}||{"level":<6}:{pokemons_2[0].lvl:>9}||{"level":<6}:{pokemons_3[0].lvl:>9}||{"level":<6}:{pokemons_4[0].lvl:>9}||{"level":<6}:{pokemons_5[0].lvl:>9}|')

    print(f'|{"XP":<6}:{pokemons_0[0].xp:>9}||{"XP":<6}:{pokemons_1[0].xp:>9}||{"XP":<6}:{pokemons_2[0].xp:>9}||{"XP":<6}:{pokemons_3[0].xp:>9}||{"XP":<6}:{pokemons_4[0].xp:>9}||{"XP":<6}:{pokemons_5[0].xp:>9}|')

    print(f'|{"lvl_UP":<6}:{pokemons_0[0].max_xp:>9}||{"lvl_UP":<6}:{pokemons_1[0].max_xp:>9}||{"lvl_UP":<6}:{pokemons_2[0].max_xp:>9}||{"lvl_UP":<6}:{pokemons_3[0].max_xp:>9}||{"lvl_UP":<6}:{pokemons_4[0].max_xp:>9}||{"lvl_UP":<6}:{pokemons_5[0].max_xp:>9}|')

    print('-' * 108)


def selection_menu(txt):
    print()
    print('*' * 100)
    print('|' + ' ' * 98 + '|')
    print('|' + f'{txt:^98}' + '|')
    print('|' + ' ' * 98 + '|')
    print('*' * 100)
    print()


def empty_bag(item):
    print()
    print('*' * 100)
    print('|' + ' ' * 98 + '|')
    print('|' + f'{f"you can not use this Item, you dont have enough {item}!":^98}' + '|')
    print('|' + ' ' * 98 + '|')
    print('*' * 100)
    print()


def bag(player):
    print()
    print('*' * 100)
    print('|' + ' ' * 98 + '|')
    print('|' + f'{"This is your bag, here you can find a choose the items you wanna use in your Pokemons":^98}' + '|')
    print('|' + f'{"Press the number of each item you want to use on this pokemon":^98}' + '|')
    print('|' + ' ' * 98 + '|')
    print('-' * 100)
    print('|' + f'{"HP Potions":^49}' + '||' + f'{"XP Potions":^47}' + '|')
    print('-' * 100)
    print('| 0 - ' + f'{"Potions        (Regenerates 20 HP)    =>":<15}' + f'{player.potions:>4}' +         '|| 4 - ' f'{"Small XP Potions  (Gives 50 XP)     =>":<12}' + f'{player.xp_potions_s:>4}' + '|')
    print('| 1 - ' + f'{"Super Potions  (Regenerates 50 HP)    =>":<9}'  + f'{player.super_potions:>4}' +   '|| 5 - ' f'{"Medium XP Potions (Gives 200 XP)    =>":<11}' + f'{player.xp_potions_m:>4}' + '|')
    print('| 2 - ' + f'{"Hyper Potions  (Regenerates 200 HP)   =>":<9}'  + f'{player.hyper_potions:>4}' +   '|| 6 - ' f'{"Large Potions     (Gives 600 XP)    =>":<11}' + f'{player.xp_potions_l:>4}' + '|')
    print('| 3 - ' + f'{"Max Potions    (Regenerates ALL HP)   =>":<11}' + f'{player.max_potions:>4}' +     '||' f'{" " * 47}' + '|')
    print('*' * 100)


def error_message(txt):
    print('*' * 100)
    print('|' + ' ' * 98 + '|')
    print('|' + '\033[1;91m' + f'{"ERROR":^98}' + '\033[m' + '|')
    print('|' + ' ' * 98 + '|')
    print('|' + '\033[1;91m' + f'{txt:^98}' + '\033[m' + '|')
    print('|' + ' ' * 98 + '|')
    print('*' * 100)