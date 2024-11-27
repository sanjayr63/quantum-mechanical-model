import numpy as np
import matplotlib.pyplot as plt
# Constants
L = 1.0 # Length of the box
N = 1000 # Number of points for the wavefunction
x = np.linspace(0, L, N)
# Function to calculate the wavefunction
def psi(n, x, L):
 return np.sqrt(2.0 / L) * np.sin(n * np.pi * x / L)
# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
fig.suptitle("Particle in a Box - Quantum Mechanics")
# Plot the wavefunction
n = 1 # Quantum number
wavefunction = psi(n, x, L)
ax1.plot(x, wavefunction, label=f'ψ{str(n)}(x)')
ax1.set_title("Wavefunction")
ax1.set_xlabel("Position (x)")
ax1.set_ylabel("ψ(x)")
# Plot the probability density
probability_density = wavefunction**2
ax2.plot(x, probability_density, label=f'|ψ{str(n)}(x)|^2', color='orange')
ax2.set_title("Probability Density")
ax2.set_xlabel("Position (x)")
ax2.set_ylabel("|ψ(x)|^2")
# Highlight the box boundaries
ax1.axvline(x=0, color='k', linestyle='--', label='Box Boundaries')
ax1.axvline(x=L, color='k', linestyle='--')
ax2.axvline(x=0, color='k', linestyle='--', label='Box Boundaries')
ax2.axvline(x=L, color='k', linestyle='--')
# Add legends
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()