my_dict = {"Глаза" : 2, "Нос" : 1, "Пальцы" : 10}
print("Части тела: ",my_dict)
print("В списке есть: ",my_dict["Нос"])
print("В списке: ",my_dict.get("Ухо","Нет такого"))
my_dict.update({"Зубы" : 32, "Кости" : 230})
a = my_dict.pop("Нос")
print("Удалим: ",a)
print("Измененный словарь: ",my_dict)

my_set = {1,2,3,4,5,6,7,8,9,9,8,7,7,7,26,53,14,3,2,1}
print("------------\n","Множество: ",my_set)
my_set.add(99)
my_set.add(111)
my_set.remove(1)
print("Измененное множество: ",my_set)