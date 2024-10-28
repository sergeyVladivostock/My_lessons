
spb = 0
def luck_spb(p):
    p = [int(i) for i in str(p)]
    print(p)
    global spb

    if len(p)%2 == 0:
        x = 0
        y = 0

        for i in p[0::2]:
            x += i
        for j in p[1::2]:
            y +=j

        if x == y:
            print('Счастливый билет (по питерской версии)')
            spb += 1

        else:
            print('Обычный билет :(')

    else:
        print('Номер билета должен быть кратным 2')

if __name__ == "__main__":

    luck_spb(f)