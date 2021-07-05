from game_functions import damage
from lists import get_damage


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.max_xp = 100
        self.lvl = 1
        self.health = 20
        self.max_health = 20

    def level_up(self):
        if self.xp >= self.max_xp:
            self.lvl        += 1
            self.max_xp     *= self.lvl
            self.max_health *= 1.5
            self.health == self.max_health

    def atack(self, opponent):
        intensity = get_damage(self.type, opponent.type)
        d1 = damage(opponent.max_health, intensity)          
        opponent.health -= d1
        return opponent.health
            

class Normal(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'normal'


class Fire(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;91m{name}\033[m'
        self.type = 'fire'      


class Water(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;34m{name}\033[m'
        self.type = 'water'


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


class Poison(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'poison'


class Ground(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;33m{name}\033[m'
        self.type = 'ground'


class Flying(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'flying'


class Psychic(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'psychic'


class Bug(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'bug'


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


class Steel(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'steel'


class Fairy(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'fairy'
