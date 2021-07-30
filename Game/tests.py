from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random import choice


p = Player('Yure')
p1 = Charizard

p1.initial_level(60)

print(p1.health)
p1.health -= 201
print(p1.health)

b = str(input('>>> '))

p1.use_potions(p, b)

print(p1.health)
