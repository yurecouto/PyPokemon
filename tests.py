from structure_functions import *
from classes import *


bulbasaur    = Grass('Bulbasaur')
charmander   = Fire('Charmander')
pikachu      = Electric('Pikachu')
eevee        = Normal('Eevee')
gengar       = Ghost('Gengar')
squirtle     = Water('Squirtle')

eevee.xp += 20
eevee.level_up()

main_interface(eevee, charmander)

eevee.xp += 40
eevee.level_up()

print(eevee.lvl)
print(eevee.health)
print(eevee.max_health)

main_interface(eevee, charmander)

eevee.xp += 40
eevee.xp += 40
eevee.level_up()

main_interface(eevee, charmander)

print(eevee.max_health)
print(eevee.health)
print(eevee.max_xp)
print(eevee.xp)
print(eevee.lvl)

