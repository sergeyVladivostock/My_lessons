from random import sample
from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'Название {self.name}, вес {self.weight}, категория {self.category}'


class Shop:
    def __init__(self, __file_name):
        self.file_name = 'product.txt'

    def get_products(self):
        self.file_name = open(self.file_name, 'r')
        pprint(self.file_name.read())
        self.file_name.close()


    def add(self, *product):
        super().__init__(product)
        self.product = product
        self.file_name = self.file_name.write(self.product())


if __name__ == '__main__':

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())


# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables