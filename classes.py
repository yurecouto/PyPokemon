from random import randint
from game_functions import damage


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.lvl = 1
        self.health = 100
        self.max_health = 100


class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'normal'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire water grass electric ice fighting poison ground flying psychic bug dragon dark fairy':
            d1 = damage(opponent.max_health) 
            opponent.health -= d1
            return opponent.health

        #Weak Atack
        elif opponent.type in 'rock steel':
            d1 = damage(opponent.max_health, 2, 12)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'ghost':
            opponent.health -= 0                      
            return opponent.health


class Fire(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;91m{name}\033[m'
        self.type = 'fire'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal electric fighting poison ground flying psychic ghost dark fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fire water rock dragon':
            d1 = damage(opponent.max_health, 2, 12)   #Weak Atack
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'grass ice bug steel':
            d1 = damage(opponent.max_health, 10, 50)   
            opponent.health -= d1
            return opponent.health


class Water(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;34m{name}\033[m'
        self.type = 'water'

    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal electric ice fighting poison flying psychic bug ghost dark steel fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'water grass dragon':
            d1 = damage(opponent.max_health, 2, 12)   #Weak Atack
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'frie ground rock':
            d1 = damage(opponent.max_health, 10, 50)   
            opponent.health -= d1
            return opponent.health


class Grass(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;92m{name}\033[m'
        self.type = 'grass'


class Electric(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;93m{name}\033[m'
        self.type = 'electric'


class Ground(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;33m{name}\033[m'
        self.type = 'ground'


class Steel(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'steel'


class Ice(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'ice'


class Fighting(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'fighting'


class Flying(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'flying'


class Poison(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'poison'


class Bug(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'bug'


class Psychic(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'psychic'


class Rock(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'rock'


class Ghost(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'ghost'


class Dragon(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'dragon'


class Dark(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'dark'


class Fairy(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'fairy'
