def title():
    '''print(
          '────────g###########h────────\n'
          '─────g###@@@@@@@@@@@###h─────\n'
          '────###@@@@@@@@@@@@@@@###────\n'
          '───##@@@@@@@@@@@@@@@@@@@##───\n'
          '──##@@@@@@@@@@@@@@@@@@@@@##──\n'
          '─##@@@@@@@@@@@@@@@@@@@@@@@##─\n'
          '##@@@@@@@@@#######@@@@@@@@@##\n'
          '##@@@@@@@@##HHHHH##@@@@@@@@##\n'
          '##@@@@@@@##HH###HH##@@@@@@@##\n'
          '###########HH###HH###########\n'
          '##HHHHHHH##HH###HH##HHHHHHH##\n'
          '##HHHHHHHH##HHHHH##HHHHHHHH##\n'
          '##HHHHHHHHH#######HHHHHHHHH##\n'
          '─##HHHHHHHHHHHHHHHHHHHHHHH##─\n'
          '──##HHHHHHHHHHHHHHHHHHHHH##──\n'
          '───##HHHHHHHHHHHHHHHHHHH##───\n'
          '────###HHHHHHHHHHHHHHH###────\n'
          '─────a###HHHHHHHHHHH###a─────\n'
          '────────a###########a────────\n'
            )'''

    print('=' * 100)
    print(
          '\033[1;91m|                                                  .::.                                            |\n'
          '|                                                .;:***            AMC                             |\n'
          '|                                                `                  0                              |\n'
          '|                    .:XHHHHk.              db.   .;;.     dH  MX   0                              |\n'
          '|                  oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN                       |\n'
          '|                  QMMMMMb  MMX       MMMMMMP !MX`  :M~   MMM MMM  .oo. XMMM `MMM                  |\n'
          '|                    `MMMM.  )M> :X!Hk. MMMM   XMM.`   .  MMMMMMM X?XMMM MMM>!MMP                  |\n'
          '|                     `MMMb.dM! XM M`?M MMMMMX.`MMMMMMMM~ MM MMM XM `  MX MMXXMM                   |\n'
          '|                      ~MMMMM~ XMM. .XM XM` MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP                   |\n'
          '|                       ?MMM>  YMMMMMM! MM   `?MMRb.    ````   !L MMMMM XM IMMM                    |\n'
          '|                        MMMX   `MMMM`  MM       ~%:           !Mh.``` dMI IMMP                    |\n'
          '|                        `MMM.                                             IMX                     |\n'
          '|                         ~M!M                                             IMP                     |\033[m'
          )


def main_interface(p_1, p_2, mh_1, mh_2, h_1, h_2, xp_1, xp_2):
    print('=' * 100)
    print('=' * 100)
    print(f'|{p_1:^58}||{p_2:^58}|')
    print('=' * 100)

    print(f'|{"Status":^48}||{"Status":^48}|')

    print(f'| Health...................{health_bar(mh_1, h_1)}||'
          f' Health...................{health_bar(mh_2, h_2):}|')

    print(f'| XP.......................{xp_bar(xp_1, 100)}||'
          f' XP.......................{xp_bar(xp_2, 100)}|')

    '''print(f'| * Level {l_1:39}|| * Level {l_2:39}|')
       print(f'| * XP {x_1:42}|| * XP {x_2:42}|')'''
    print('=' * 100)


def game_interface(my_pokemon):
    atack = '\033[1;91mATACK\033[m'
    capture = '\033[1;92mCAPTURE\033[m'
    bag = '\033[1;93mBAG\033[m'

    print(f'|{"Options":^98}|')
    print('=' * 100)

    print(f"|{f'My Pokemon: {my_pokemon}!':^108}|")

    print(f'|{" " * 98}|')
    print(f"|{f'Press 1 for {atack} | 2 to try to {capture} | 3 to see your {bag}':^128}|")
    print('=' * 100)


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


title()