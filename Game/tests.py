from structure_functions    import *
from game_functions         import *
from classes                import *
from pokemons               import *
from lists                  import *
from random                 import choice, sample

for p in range(0, len(object_forest)):
    sorteados = sample(object_forest, 4)
    print(sorteados)

