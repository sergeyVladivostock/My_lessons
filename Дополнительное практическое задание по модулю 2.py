import random
a = random.randint(3, 20)
b = []
v = []
q = []
for i in range(1,a+1):
    b.append(i)
    v.append(i)
for i in range(1,len(b)) :
    for j in range(1,len(b)+1):
        if a % (i +j) == 0 and a!=j and i < j :
            if j != i:
                q.append(i)
                q.append(j)
            if i > (a/2):
                break
print(a,' -- ',*q)
