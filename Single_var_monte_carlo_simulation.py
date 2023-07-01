import random

def monte_carlo_simulation(n, num_simulations=100000):
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

# number of unique couples
n = 50

# run the simulation
average_boxes = monte_carlo_simulation(n)
print(f'Average boxes needed to get all {n} unique couples: {average_boxes}')
