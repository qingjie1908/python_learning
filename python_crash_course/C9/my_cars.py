from class_electrical_car import ElectricCar
from class_electrical_car import Car

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# 2024 Ford Mustang
# 2024 Nissan Leaf

# Alias
from class_electrical_car import ElectricCar as EC
my_car1 = EC('nissan', 'leaf', 2024)

import class_electrical_car as ec
my_car2 = ec.ElectricCar('nissan', 'leaf', 2024)

from random import randint
m = randint(1, 5)
# print(m) # 5