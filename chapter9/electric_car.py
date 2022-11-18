"""A set of classes that can be used to represent electric cars."""
from car import Car    

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# my_tesla = ElectricCar('tesla', 'model s', '2019')
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()