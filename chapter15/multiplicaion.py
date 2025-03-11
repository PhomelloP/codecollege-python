import random
import matplotlib.pyplot as plt

def multiply_two_d6(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        results.append(roll1 * roll2)
    return results

def plot_results_multiplication(results):
    plt.hist(results, bins=range(1, 37), edgecolor='black', align='left')
    plt.xlabel('Product of Two D6')
    plt.ylabel('Frequency')
    plt.title('Distribution of Product of Two D6 (1,000 Rolls)')
    plt.xticks(range(1, 37))
    plt.show()

num_rolls = 1000
results = multiply_two_d6(num_rolls)
plot_results_multiplication(results)


