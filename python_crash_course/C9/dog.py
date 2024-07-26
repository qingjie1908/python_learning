class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, p_name, p_age) -> None:
        """Initialize name and age attributes."""
        self.name = p_name
        self.age = p_age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
# My dog's name is Willie.
# My dog is 6 years old.
# Willie is now sitting.
# Willie rolled over!

my_dog.age = 7
print(f"My dog is {my_dog.age} years old now.")