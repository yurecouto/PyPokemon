from classes import *
from functions import *

charmander = Fire('Charmander')
squirtle = Water('Squirtle')
bulbasaur = Grass('Bulbasaur')
pikachu = Electric('Pikachu')

while pikachu.health > 0:

    main_interface(charmander.name,         pikachu.name,
                   charmander.max_health,   pikachu.max_health,
                   charmander.health,       pikachu.health,
                   charmander.xp,           pikachu.xp)

    game_interface(bulbasaur.name)

    action = int(input('>>> '))

    while action == 1:
        charmander.atack(pikachu)
        break
