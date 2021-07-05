from random import randint

def damage(base, intensity):
    min_d = 5  * intensity
    max_d = 25 * intensity
    atack = randint(((base * min_d) / 100), (base * max_d) / 100)
    return int(atack)
