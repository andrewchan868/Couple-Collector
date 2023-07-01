import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_simulation(n, num_simulations=1000):
    total_boxes = 0
    for _ in range(num_simulations):
        found = [False] * n
        count = 0
        while not all(found):
            couple = random.randint(0, n-1)
            found[couple] = True
            count += 1
        total_boxes += count
    average_boxes = total_boxes / num_simulations
    return average_boxes

n_values = list(range(10, 201, 10))
average_boxes_values = [monte_carlo_simulation(n) for n in n_values]

# Plot the simulation results
plt.plot(n_values, average_boxes_values, label='Monte Carlo Simulation')

# Plot the harmonic series
harmonic_values = [n * sum(1.0/i for i in range(1, n+1)) for n in n_values]
plt.plot(n_values, harmonic_values, label='Harmonic Series')

plt.xlabel('n (number of unique coupons)')
plt.ylabel('Average number of boxes')
plt.title('Number of boxes needed to get all unique coupons')
plt.legend()
plt.grid(True)
plt.show()
