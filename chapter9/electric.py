from Cars import Car as parent_class
from battery import Battery as smaller_variable

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, Make, Model, Year):
        """Initialize attributes of the parent class."""
        super().__init__(Make, Model, Year)
        self.battery_size = 75  # Default battery size in kWh

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank.")
