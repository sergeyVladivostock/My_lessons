grades = [ ["Алексей", 5, 4, 3], ["Мария", 4, 5, 5], ["Иван", 3, 2, 4], ["Елена", 5, 5, 5] ] #список
l = -1 #индекс вложенного списка
f = len(grades) # кол-во влаженных списков
g = len(grades[l]) # длинна вложенного списка
z = 0 #
x = {} #словарь
list_name = [] # список ключей
h = [[]for d in range(f)] #
b = [[] for r in range(f)] #
for i in grades: # создаются списки с ключами и значениями
    l += 1
    for j in i:
        c = i.index(j) #определяем ключ это или значение по индексу
        if c == 0:
            list_name.append(j) # список ключей
        else:
            b[l].append(j) # список значений
l = -1
for s in b: # вычмсление средней оценки
    l += 1
    for d in s:
        z = z + d
    z = z / len(b[0])
    h[l].append(z)
    z = 0
for k in range(f):
    x[list_name[z]] = h[z]
    z +=1
print(x)
print("=======================================")
p = [] # пустой список для средних оценок
t=(x.keys())
for i in t: #заполняем пустой список значениями средних оценок
    x.get(i)
    p.append(x.get(i))
z = max(p) # присваеваем переменной наивысшую среднюю оценку из списка
k = 0
for i in x: # сравниваем оценку из словаря с высшей средней
    if x[list_name[k]] < z:
        k += 1
        continue
    if x[list_name[k]] == z:
        print(list_name[k],"!",z)
        break