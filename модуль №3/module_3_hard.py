def calculate_structure_sum(*args):
    print(*data_structure)
    print(type(data_structure))
    n=0
    for i in data_structure:
        if isinstance(i, list):
            b = sum(i)
            n = n + b

        if isinstance(i, dict):
            c = 0
            for j in i:
                c += len(j)
                c += i.get(j)

            n = n+c

        if isinstance(i, str):
            b= len(i)
            n = b + n
        if isinstance(i, tuple):
            calculate_structure_sum(i)




data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
