import random
import matplotlib.pyplot as plt

#Simulate Dice rolls
def roll_three_d6(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        results.append(roll1 + roll2 + roll3)
    return results

#visualize the results

def plot_results_three_d6(results):
    plt.hist(results, bins=range(3, 19), edgecolor='black', align='left')
    plt.xlabel('Sum of Three D6')
    plt.ylabel('Frequency')
    plt.title('Distribution of Sum of Three D6 (1,000 Rolls)')
    plt.xticks(range(3, 19))
    plt.show()

num_rolls = 1000
results = roll_three_d6(num_rolls)
plot_results_three_d6(results)
