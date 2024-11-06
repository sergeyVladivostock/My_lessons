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

    def describe_user(self):
        print(f'Имя: {self.first_name} \nФамилия: {self.last_name} \nВозраст: {self.age} \nЦвет: {self.color}\n')

    def greet_user(self):
        print(f'Привет {self.first_name}\n')

if __name__ == '__main__':



     restaurant1 = Restaurant('1', '4')
    # restaurant1.describe_restaurant()
    # restaurant1.open_restaurant()
    # r2 = Restaurant(5, 12)
    # r2.describe_restaurant()
    # r3 = Restaurant('wer', 'dfg')
    # r3.describe_restaurant()

    # u1 = User("Сергей", "Бажан", 38, 'Black')
    # u2 = User("Андрей", "Боорщев", 32, "Blue")
    # u1.describe_user()
    # u1.greet_user()
    # u2.describe_user()
    # u2.greet_user()
