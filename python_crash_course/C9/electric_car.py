class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if(mileage >= self.odometer_reading):
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car has a gas tank!")

# Inheritence
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year) -> None:
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)

        """Then initialize attributes specific to an electric car."""
        self.battery_size = 40

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# 2024 Nissan Leaf

my_leaf.describe_battery()
# This car has a 40-kWh battery.

my_leaf.fill_gas_tank()
# This car doesn't have a gas tank!
my_car = Car('audi', 'a4', 2024)
my_car.fill_gas_tank()
# This car has a gas tank!
