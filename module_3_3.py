def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
    # print(a,b)
    # print(a)
    # print()
    # print(b = 25)
    # print(c = [1, 2, 3])

print_params()

print("===============================")

values_list = (1 , True, "Fool")
values_dict = {'a': False, 'b': 23, 'c': 'Marvel'}

print_params(*values_list)
print_params(**values_dict)

print("===============================")

values_list_2 = (True, 77)
print_params(*values_list_2, 99)