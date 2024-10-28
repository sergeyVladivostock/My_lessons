import random
from Luck_tiket.LUCK.LUCK import *


def luck_krd(k):
    k = [int(i) for i in str(k)]
    print(k)
    krdr = 0

    if len(k) >= 6:
        x = 0
        y = 0

        for i in k[0:3]:
            x += i
        for j in k[:-4:-1]:
            y +=j

        if x == y:
            print('Счастливый билет (по краснодарской версии)')
            krdr += 1

        else:
            print('Обычный билет :(')

    else:
        print('Номер билета должен быть не менее 6 знаков')

    if __name__ == "__main__":
        luck_krd(f)
