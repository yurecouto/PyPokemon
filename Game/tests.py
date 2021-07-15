from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *

p1 = Charizard

p1.xp += 55
p1.level_up()  

p1.xp += 80
p1.level_up()   

p1.xp += 120
p1.level_up()

print(p1.xp)
print(p1.max_xp)
print(p1.health)
print(p1.max_health)
print(p1.lvl)