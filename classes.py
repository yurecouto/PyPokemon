from game_functions import damage
from lists import xp_list


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.max_xp = 100
        self.lvl = 1
        self.health = 100
        self.max_health = 100

    # criar lista definindo o max xp, e iterar ela dentro do metodo level up
    def level_up(self):
        if self.xp >= self.max_xp:
            self.lvl += 1
            

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
            d1 = damage(opponent.max_health, 2, 12) 
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'grass ice bug steel':
            d1 = damage(opponent.max_health, 15, 45)   
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
        elif opponent.type in 'fire ground rock':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Grass(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;92m{name}\033[m'
        self.type = 'grass'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal electric ice fighting psychic ghost dark fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fire grass poison flying bug dragon steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'water ground rock':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Electric(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;93m{name}\033[m'
        self.type = 'electric'
        
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire ice fighting poison psychic bug rock ghost dark steel fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'grass electric dragon':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'water flying':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'ground':
            opponent.health -= 0                      
            return opponent.health


class Ice(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'ice'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal electric fighting poison psychic bug rock ghost dark fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fire water ice steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'grass ground flying dragon':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Fighting(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'fighting'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'fire water grass electric fighting ground dragon':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'poison flying psychic bug fairy':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'normal ice rock dark steel':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'ghost':
            opponent.health -= 0                      
            return opponent.health


class Poison(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'poison'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire water electric ice fighting flying psichic bug dragon dark':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'poison ground rock ghost':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'grass fairy':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'steel':
            opponent.health -= 0                      
            return opponent.health


class Ground(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;33m{name}\033[m'
        self.type = 'ground'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal water ice fighting ground psychic ghost dragon dark fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'grass bug':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'fire electric poison rock steel':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'flying':
            opponent.health -= 0                      
            return opponent.health


class Flying(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'flying'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire water ice poison ground flying psychic ghost dragon dark fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'electric rock steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'grass fighting bug':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Psychic(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'psychic'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire water grass electric ice ground flying bug rock ghost dragon fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'psychic steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'fighting poison':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'dark':
            opponent.health -= 0                      
            return opponent.health


class Bug(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'bug'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal water electric ice ground bug rock dragon':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fire fighting poison flying ghost steel fairy':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'grass psychic dark':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Rock(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'rock'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal water grass electric poison psychic rock ghost dragon dark fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fighting ground steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'fire ice flying bug':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Ghost(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'ghost'


    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'fire water grass electric ice fighting poison ground flying bug rock dragon steel fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'dark':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'psychic ghost':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'normal':
            opponent.health -= 0                      
            return opponent.health


class Dragon(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'dragon'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire water grass electric ice fighting poison ground flying psychic bug rock ghost dark':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'dragon':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health

        #No Effective Atack
        elif opponent.type in 'fairy':
            opponent.health -= 0                      
            return opponent.health


class Dark(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'dark'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal fire water grass electric ice poison ground flying bug rock dragon steel':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fighting dark fairy':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'psychic ghost':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Steel(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'steel'

    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal grass fighting poison ground flying psychic bug ghost dragon dark':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fire water electric steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'ice rock fairy':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health


class Fairy(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.name = f'\033[1;37m{name}\033[m'
        self.type = 'fairy'
    
    def atack(self, opponent):
        #Normal Atack
        if opponent.type in 'normal water grass electric ice ground flying psychic bug rock ghost fairy':
            d1 = damage(opponent.max_health)          
            opponent.health -= d1
            return opponent.health   

        #Weak Atack
        elif opponent.type in 'fire poison steel':
            d1 = damage(opponent.max_health, 2, 12)
            opponent.health -= d1
            return opponent.health

        #Strong Atack
        elif opponent.type in 'fighting dragon dark':
            d1 = damage(opponent.max_health, 15, 45)   
            opponent.health -= d1
            return opponent.health
