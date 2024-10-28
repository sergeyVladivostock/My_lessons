from operator import index


def stroka(str1):
    a = '('
    c = ')'
    b = 0
    for i in range(0,len(str1),2):
        if str1[i] == a and i != len(str1)-1:
            for j in reversed(str1):
                f = str1.index(j)
                if str1[f] == c:
                    continue
                else:
                    b += 1
                    break
        else:
            b +=1
            break
    if b == 0:
        print(True)
    else:
        print(False)
stroka('(())')
