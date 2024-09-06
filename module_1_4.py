my_string = input("Введите текст из двух и более слов: ")
print("Количество символов: ", len(my_string))

print("Верхний регистр: ", my_string.upper(),
      "\nНижний регистр: ", my_string.lower(),
      "\nСтрока без пробелов: ", my_string.replace(" ", ""),
      "\nПервый символ строки: ", my_string[0],
      "\nПоследний символ строки: ", my_string[-1])

