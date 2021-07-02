from structure_functions import *
from classes import *

charmander = Fire('Charmander')
pikachu = Electric('Pikachu')

min_atack = (charmander.health * 10) / 100
max_atack = (charmander.health * 30) / 100

while True:
    main_interface(charmander, pikachu)

    action_test = int(input('>>> '))

    while action_test == 1:
        charmander.atack(pikachu, min_atack, max_atack)
        break
