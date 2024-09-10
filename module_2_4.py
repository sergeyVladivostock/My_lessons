numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
d = 0 # кол-во делителей
f = len(numbers) # длинна списка
for i in numbers:
    if i != 1:
        for j in range(0,f) :
            if j == 0:
                j = j + 1
            elif i % j == 0 and d <= 2:
                d += 1
                if d > 2:
                    break
        if d <= 2:
            primes.append(i)
            d = 0
            continue
        if d > 2:
            not_primes.append(i)
            d = 0
            continue
print("простые числа",primes)
print("не простые числа",not_primes)