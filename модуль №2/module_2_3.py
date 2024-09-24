my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Index = 0
Long = len(my_list)
while Index < Long :
    if my_list[Index] > 0:
        print(my_list[Index])
        Index = Index + 1
    elif my_list[Index] == 0:
        Index = Index + 1
        continue
    else:
        break
