class Restaurant:

    def  __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name}')
        print(f'{self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт')

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

if __name__ == '__main__':
    u1 = User('Sergey', 'Bazhan', 38, 'Blue')
    for i in range(7):
        u1.increment_login_attempts()
    print(u1.login_attempts)
    u1.reset_login_attempts()
    print(u1.login_attempts)
