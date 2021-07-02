from random import randint


def damage(base):
    atack = randint(((base * 10) / 100), (base * 30) / 100)
    return atack


print(damage(100))