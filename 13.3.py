class Restaurant:

    def  __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name}')
        print(f'{self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт')

class IceCreamStand(Restaurant):

    def __init__(self, *flavors):
        self.flavors = flavors

    def  ice_set(self):
        for i in self.flavors:
            print(i)

class User:

    def __init__(self, first_name, last_name, age, color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.color = color
        self.login_attempts = 0

    def describe_user(self):
        print(f'Имя: {self.first_name} \nФамилия: {self.last_name} \nВозраст: {self.age} \nЦвет: {self.color}\n')

    def greet_user(self):
        print(f'Привет {self.first_name}\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin

i1 = IceCreamStand('blue', 'black', 'yellow')
i1.ice_set()