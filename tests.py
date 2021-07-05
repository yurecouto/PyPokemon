from structure_functions import *
from classes import *


bulbasaur    = Grass('Bulbasaur')
charmander   = Fire('Charmander')
pikachu      = Electric('Pikachu')
eevee        = Normal('Eevee')
gengar       = Ghost('Gengar')

eevee.atack(gengar)
charmander.atack(bulbasaur)

eevee.xp = 120
eevee.level_up()

print(eevee.lvl)