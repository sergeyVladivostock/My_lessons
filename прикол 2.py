
grades = [ ["Алексей", 5, 4, 3], ["Мария", 4, 5, 5], ["Иван", 3, 2, 4], ["Елена", 5, 5, 5] ] #список
x = {}
p  = []
for i in grades:
    for j in i:
        if isinstance(j,str) == True:
            x[j] = None
        else:
            f = i.index(j)
            if i.index(j) != 0 and i.index(j) < 2:
                a = list(x.keys())
                x[a[-1]] = sum(i[1:len(i)])/(len(i)-1)
print(x)
print("=======================================")
t=(x.keys())
for i in t:
    x.get(i)
    p.append(x.get(i))
z = max(p)
k = 0
for i in x:
    if x[a[k]] < z:
        k += 1
        continue
    if x[a[k]] == z:
        print(a[k],"!",z)
        break