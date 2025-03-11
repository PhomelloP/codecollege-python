import random
import matplotlib.pyplot as plt

def roll_two_d8s(num_rolls):
    return [random.randint(1, 8) + random.randint(1, 8) for _ in range(num_rolls)]

def roll_three_d6(num_rolls):
    return [random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) for _ in range(num_rolls)]

def multiply_two_d6(num_rolls):
    return [random.randint(1, 6) * random.randint(1, 6) for _ in range(num_rolls)]
