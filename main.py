from time import sleep
from classes import *
from structure_functions import *

while True:
    charmander = Fire('Charmander')
    squirtle = Water('Squirtle')
    bulbasaur = Grass('Bulbasaur')
    pikachu = Electric('Pikachu')

    title()
    main_menu()

    game = int(input('>>> '))

    while game == 1:
        initial_menu(bulbasaur.name, squirtle.name, charmander.name, pikachu.name)

        initial_pokemon = str(input('>>> '))

        while initial_pokemon.upper() == 'CHARMANDER':
            p1 = charmander
            p2 = pikachu

            while True:
                game_interface(p1)
                main_interface(p1, p2)

                action = int(input('>>> '))

                while action == 1:
                    p1.atack(p2)
                    break

                p2.atack(p1)


