import numpy as np
import matplotlib.pyplot as plt

def logistic_growth(time, carrying_capacity, growth_rate, lag_phase_range, exp_phase_range):
    lag_phase_length = np.random.randint(*lag_phase_range)
    exp_phase_length = np.random.randint(*exp_phase_range)
    
    population = np.zeros_like(time, dtype=float)

    for i, t in enumerate(time):
        if t < lag_phase_length:
            population[i] = 1  # Initial small population
        elif t < lag_phase_length + exp_phase_length:
            population[i] = 1 * np.exp(growth_rate * (t - lag_phase_length))
        else:
            population[i] = carrying_capacity / (1 + ((carrying_capacity - 1) / 1) * np.exp(-growth_rate * (t - lag_phase_length - exp_phase_length)))

    return population

# Example Usage
time = np.linspace(0, 50, 100)
growth_curve = logistic_growth(time, carrying_capacity=1000, growth_rate=0.2, lag_phase_range=(3, 8), exp_phase_range=(10, 15))

# Plot the Growth Curve
plt.figure(figsize=(8, 5))
plt.plot(time, growth_curve, label="Logistic Growth Curve", color="blue")
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.title("Logistic Growth Curve Simulation")
plt.legend()
plt.show()
