import car2


my_tesla = car2.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print('')
my_beetle = car2.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())