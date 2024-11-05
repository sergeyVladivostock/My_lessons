class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('Fuck you!!!')

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):

    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.
                Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """Выводит информацию о мощности аккумулятора."""
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.update_odometer(44)
# my_new_car.read_odometer()

# my_used_car = Car("subaru", 'outback', 2013)
# print((my_used_car.get_descriptive_name()))
# my_used_car.update_odometer(23500)
# my_used_car.read_odometr()
# my_used_car.increment_odometer(-5)
# my_used_car.read_odometr()


