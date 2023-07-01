import random

def monte_carlo_simulation(num_simulations=200000):
    total_throws = 0
    for _ in range(num_simulations):
        found = [False] * 6
        count = 0
        while not all(found):
            face = random.randint(0, 5)
            found[face] = True
            count += 1
        total_throws += count
    average_throws = total_throws / num_simulations
    return average_throws

# run the simulation
average_throws = monte_carlo_simulation()
print(f'Average throws needed to get all 6 faces: {average_throws}')
