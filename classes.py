from random import randint


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.lvl = 1
        self.health = 100
        self.max_health = 100

    def atack(self, pokemon):
        damage = 25
        pokemon.health -= damage
        return pokemon.health


class Fire(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;91m{name}\033[m'


class Water(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;34m{name}\033[m'


class Grass(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;92m{name}\033[m'


class Electric(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;93m{name}\033[m'


class Ground(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;33m{name}\033[m'


class Steel(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
