
msc = 0
def luck_msc(m):
    m = [int(i) for i in str(m)]
    print(m)
    global msc
    if len(m)%2 == 0:
        x = 0
        y = 0
        for i in m[0:len(m)//2]:
            x += i
        for j in m[:(len(m)//2)-1:-1]:
            y +=j
        if x == y:
            print('Счастливый билет (по московской версии)')
            msc += 1

        else:
            print('Обычный билет :(')
    else:
        print('Номер билета должен быть не менее 6 знаков')

if __name__ == "__main__":
    luck_msc(f)
