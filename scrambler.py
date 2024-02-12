import random
from constants import *


def get_random_scramble():
    scramble_length = random.randint(20, 25)

    move1 = random.choice(SCRAMBLE_MOVES)
    move2 = random.choice(SCRAMBLE_MOVES)

    while not compatible(move1, move2):
        move2 = random.choice(SCRAMBLE_MOVES)

    scramble = [move1, move2]

    for i in range(scramble_length - 2):
        move2 = get_next_move(scramble[-1], scramble[-2])
        scramble.append(move2)

    return scramble


def compatible(move1, move2):
    return CHECKER1[move1] != CHECKER1[move2]


def get_next_move(move1, move2):
    num1 = CHECKER2[move1]
    num2 = CHECKER2[move2]

    if num1 == num2:
        if num1 == 1:
            return random.choice(NOT_U_AND_D)
        if num1 == 2:
            return random.choice(NOT_R_AND_L)
        if num1 == 3:
            return random.choice(NOT_F_AND_B)
    else:
        if num1 + num2 == 3:
            return random.choice(NOT_U_AND_D_AND_R_AND_L)
        if num1 + num2 == 5:
            return random.choice(NOT_R_AND_L_AND_F_AND_B)
        if num1 + num2 == 4:
            return random.choice(NOT_F_AND_B_AND_U_AND_D)
