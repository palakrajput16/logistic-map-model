import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 1000  # Carrying capacity
P0 = 30   # Initial population
T = 10    # Time duration

# Choosing multiple values of r for comparison
r_values = [1.5, 2.5, 3.2, 3.51]

# Create figure
plt.figure(figsize=(8, 5))

# Simulate and plot for each r value
for r in r_values:
    P = np.zeros(T + 1)  
    P[0] = P0  

    for t in range(T):
        P[t + 1] = r * P[t] * (1 - P[t] / K)  # Logistic growth formula

    plt.plot(range(T + 1), P, marker='o', linestyle='-', label=f"r = {r}")

# Carrying capacity line
plt.axhline(K, color='r', linestyle='--', label="Carrying Capacity (K)")

# Labels and title
plt.xlabel("Time (t)")
plt.ylabel("Population (P)")
plt.title("Comparison of Population Growth for Different Growth Rates")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
