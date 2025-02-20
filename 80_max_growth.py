import numpy as np

def time_to_80_percent_max(time, population, carrying_capacity):
    target_population = 0.8 * carrying_capacity  # 80% of carrying capacity
    for t, pop in zip(time, population):
        if pop >= target_population:
            return t  # Return the first time reaching 80%
    return None  # If never reaches 80%

# Example Usage
time = np.linspace(0, 100, 1000)  # Simulated time points
carrying_capacity = 1000  # Example carrying capacity
population = carrying_capacity / (1 + np.exp(-0.1 * (time - 50)))  # Logistic growth curve

time_80 = time_to_80_percent_max(time, population, carrying_capacity)
print(f"Time to reach 80% of carrying capacity: {time_80:.2f}")

