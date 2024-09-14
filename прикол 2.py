grades = [ ["Алексей", 5, 4, 3], ["Мария", 4, 5, 5], ["Иван", 3, 2, 4], ["Елена", 5, 5, 5] ] #список
x = {}
p  = []
o = 0
for i in grades:
    for j in i:
        if isinstance(j,str) == True:
            x[j] = None
        else:
            f = i.index(j)
            if i.index(j) != 0 and i.index(j) < 2:
                a = list(x.keys())
                m = a[-1]
                x[m] = j
                p.append(j)

            else:
                x[m] = j


print(x)