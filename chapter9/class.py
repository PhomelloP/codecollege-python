# 9.1 9.2 
class Restaurant:
    "simple restaurant class"
    def __init__(self,restaurant_name,cuisine_type):
        """Initialize name and type"""
        self.restaurant_name=restaurant_name
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        """describes a restaurant"""
        print(f"The restaurant is called {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """prints open message"""
        print(f"The restaurant {self.restaurant_name} is open!")

Chinese_restaurant = Restaurant("Beijing Temple","Chinese")
Mzansi_restaurant= Restaurant("kWA'MAIMAI","Shisa'nyama")
American_restaurant=  Restaurant("Pitstop","American")

Chinese_restaurant.describe_restaurant()
print("----")
Mzansi_restaurant.describe_restaurant()
print("----")
American_restaurant.describe_restaurant()

#9.3 User class

class user:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")


user.profile = user('john', 'doe', 'johndoe', "johndoe@gmail.com", "Pretoria")
user.profile.describe_user()
user.profile.greet_user()

user.profile = user('jane', 'doe', 'janedoe', "janedoe@gmail.com", "Johannesburg")
user.profile.describe_user()
user.profile.greet_user()

user.profile = user(input("Enter a first name: "), input("Enter a last name: "), input("Enter a username: "), input("Enter an email: "), input("Enter a location: "))
user.profile.describe_user()
user.profile.greet_user()

#Game Character
class Character:
    "Stores game character info"
    def _init_(self,health,damage,speed):
        self.healh=health
        self.damage=damage
        self.speed=speed

Ninja= Character(100,60,90)
Alien= Character(75,80,60)
Troll= Character(80,70,50)

print(f"Ninja HEALTH IS: {Ninja.health}")
print("---FIGHT!---")

print(f"Alien HEALTH IS: {Alien.health}")
print("---FIGHT!---")

print(f"Troll HEALTH IS: {Troll.health}")

    