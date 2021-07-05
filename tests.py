from structure_functions import *
from classes import *


bulbasaur    = Grass('Bulbasaur')
charmander   = Fire('Charmander')
pikachu      = Electric('Pikachu')
eevee        = Normal('Eevee')
gengar       = Ghost('Gengar')
squirtle     = Water('Squirtle')

eevee.xp += 200
eevee.level_up()

eevee.xp += 400
eevee.level_up()

print(eevee.lvl)
print(eevee.health)
print(eevee.max_health)