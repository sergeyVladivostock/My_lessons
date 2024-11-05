class Restaurant:

    def  __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name}')
        print(f'{self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт')

    def set_number_served(self, col_vo):
        self.number_served = col_vo

    def increment_number_served(self, poset):
        self.number_served += poset

if __name__ == '__main__':
    r1 = Restaurant('Forrr', "PoP")
    print(r1.number_served)
    r1.set_number_served(12)
    print(r1.number_served)
    r1.increment_number_served(50)
    print(r1.number_served)