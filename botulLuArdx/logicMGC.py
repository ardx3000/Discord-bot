import random

aHiLow = 0;


def rollM():
    x = (random.randint(0, 100))
    return x


def daCuBanul():
    x = (random.randint(1, 2))

    if x == 1:
        return 'Cap'
    elif x == 2:
        return 'Pajura'

    return 'erroare!!! DANIEL!!!!'


def HLR():
    x = (random.randint(0, 100))
    return


def highLogic():
    global aHiLow

    x = HLR()

    if x >= aHiLow:
        return 'High won:'
    elif x < aHiLow:
        return 'High lost:'

    aHiLow = x
    return 'erroare!!! DANIEL!!!!'


def lowLogic():
    global aHiLow

    x = HLR()

    if x > aHiLow:
        return 'Low lost:'
    elif x <= aHiLow:
        return 'Low won:'

    aHiLow = x
    return 'erroare!!! DANIEL!!!!'
