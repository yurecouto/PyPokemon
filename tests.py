from structure_functions import *
from classes import *


bulbasaur    = Grass('Bulbasaur')
charmander   = Fire('Charmander')
pikachu      = Electric('Pikachu')
eevee        = Normal('Eevee')
gengar       = Ghost('Gengar')

eevee.atack(charmander)

print(charmander.health)

