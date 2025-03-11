import random
import matplotlib.pyplot as plt

def roll_two_d8s(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll1 = random.randint(1, 8)
        roll2 = random.randint(1, 8)
        results.append(roll1 + roll2)
    return results

def plot_results(results):
    plt.hist(results, bins=range(2, 18), edgecolor='black', align='left')
    plt.xlabel('Sum of Two D8s')
    plt.ylabel('Frequency')
    plt.title('Distribution of Sum of Two D8s (1,000 Rolls)')
    plt.xticks(range(2, 17))
    plt.show()

num_rolls = 10000
results = roll_two_d8s(num_rolls)
plot_results(results)
