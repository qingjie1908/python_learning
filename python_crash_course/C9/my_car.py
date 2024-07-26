from class_car import Car
from class_car import ElectricCar

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
# 2024 Audi A4

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# This car has 23 miles on it.

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
# 2024 Nissan Leaf
# This car has a 40-kWh battery.
# This car can go about 150 miles on a full charge.

# if import whole module
# import class_car
# my_car1 = class_car.Car('ford', 'mustang', '2024')
