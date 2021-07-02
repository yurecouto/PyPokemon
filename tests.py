from structure_functions import *
from classes import *


bulbasaur    = Grass('Bulbasaur')
charmander   = Fire('Charmander')
pikachu      = Electric('Pikachu')
eevee        = Normal('Eevee')
gengar       = Ghost('Gengar')

eevee.atack(gengar)
charmander.atack(bulbasaur)

print(gengar.health)
print(bulbasaur.health)
print(eevee.name)