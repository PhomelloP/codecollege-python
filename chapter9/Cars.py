#car
class Car:
    """Simple attempt to represent a car"""

    def __init__(self,Make,Model,Year):
        """Initialize attributes to creat a car"""
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns formatted descriptive name"""
        long_name= f'{self.Year} {self.Make} {self.Model}'
        return long_name.title()
    
    def read_odometer(self):
        """Prints the cars mileage"""
        print(f'This car has {self.odometer_reading} kilometers on it')

    def update_ododmeter(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't Roll back an Odometer")

    def increment_odometer(self,miles):
        """Adds to odometer reading"""
        self.odometer_reading += miles


    
    def describe_battery(self):
        """print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}--kwh battery.")

    def fill_gas_tank(self):
        """Electric cars dont have gas tanks"""
        print("This car does not need a gas tank")
        
my_tesla = ElectricCar('Tesla', 'Model S', 2018)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
my_tesla.read_odometer()

# Updating and incrementing odometer
my_tesla.update_odometer(5000)
my_tesla.increment_odometer(300)
my_tesla.read_odometer()

