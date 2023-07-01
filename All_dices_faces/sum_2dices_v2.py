import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_simulation(num_simulations=100000):
    total_throws = 0
    counts = [0]*11  # counts for each sum
    for _ in range(num_simulations):
        found = [False] * 11  # 11 possible sums (2-12)
        count = 0
        while not all(found):
            sum_dice = random.randint(1, 6) + random.randint(1, 6) - 2  # sum of two dice - 2 to fit into the array
            found[sum_dice] = True
            counts[sum_dice] += 1
            count += 1
        total_throws += count
    average_throws = total_throws / num_simulations
    return average_throws, counts

# run the simulation
average_throws, counts = monte_carlo_simulation()
print(f'Average throws needed to get all sums from 2 to 12: {average_throws}')

# Plot the number of throws needed to get all sums from 2 to 12
plt.hist([monte_carlo_simulation(num_simulations=1)[0] for _ in range(10000)], bins=range(10, 60), edgecolor='black')
plt.xlabel('Number of Throws')
plt.ylabel('Frequency')
plt.title('Number of Throws Needed to Get All Sums from 2 to 12')
plt.grid(True)
plt.show()

# Plot the occurrence of each sum
plt.bar(range(2, 13), counts)
plt.xlabel('Sum of Dice')
plt.ylabel('Occurrences')
plt.title('Occurrences of Each Sum')
plt.grid(True)
plt.show()
