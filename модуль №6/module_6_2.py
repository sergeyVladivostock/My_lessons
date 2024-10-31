

class Vehicle:

    __COLOR_VARIANTS = ['yellow', 'black','white', 'red']


    def __init__(self, owner, __model, __color , __engine):
        self.owner = str(owner)
        self.model = str(__model)
        self.engine =  int(__engine)
        self.color = str(__color)


    def get_model(self, __model):
        return f'Модель: {self.model}'

    def get_horsepower(self, __engine):
        return f'Мощность двигателя: {self.engine}'
    def get_color(self, __color):
        return f'Цвет: {self.color}'
    def print_info(self):
        print(f' Модель: {self.model} \n Мощность двигателя: {self.engine} \n Цвет: {self.color} \n Владелец: ', self.owner)

    def set_color(self, new_color):
        if str.lower(new_color) in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(" Нельзя сменить цвет на ", new_color)



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok
