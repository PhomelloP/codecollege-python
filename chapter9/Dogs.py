class Dog:
    """A simple class to represent a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def bark(self):
        """Simulate the dog barking."""
        print(f"{self.name} is barking!")

class GoldenRetriever(Dog):
    """Represent aspects of a dog, specific to Golden Retrievers."""

    def __init__(self, name, age):
        """Initialize attributes of the parent class."""
        super().__init__(name, age)

    def fetch(self):
        """Simulate the dog fetching an item."""
        print(f"{self.name} is fetching the ball!")

