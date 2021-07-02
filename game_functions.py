from random import randint


def damage(base, min_d=5, max_d=25):
    atack = randint(((base * min_d) / 100), (base * max_d) / 100)
    return int(atack)

