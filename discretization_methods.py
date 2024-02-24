import numpy as np
import matplotlib.pyplot as plt

# Parameters for the geometric Brownian motion
r = 0.05  # drift coefficient
sigma = 0.2  # diffusion coefficient
T = 1.0  # total time
N = 100  # number of time steps
dt = T/N  # time step size
S0 = 1  # initial value of the asset

# Time points
t = np.linspace(0, T, N+1)

# Function for Euler discretization of geometric Brownian motion
def euler_discretization(S0, r, sigma, dt, N):
    S = np.zeros(N+1)
    S[0] = S0
    for i in range(1, N+1):
        Z = np.random.normal(0, 1)  # standard normal random variable
        S[i] = S[i-1] * (1 + r*dt + sigma*np.sqrt(dt)*Z)
    return S

# Function for Milstein discretization of geometric Brownian motion
def milstein_discretization(S0, r, sigma, dt, N):
    S = np.zeros(N+1)
    S[0] = S0
    for i in range(1, N+1):
        Z = np.random.normal(0, 1)  # standard normal random variable
        S[i] = S[i-1] * (1 + r*dt + sigma*np.sqrt(dt)*Z + 0.5*sigma**2*(Z**2 - 1)*dt)
    return S

# Perform the Euler discretization
S_euler = euler_discretization(S0, r, sigma, dt, N)

# Perform the Milstein discretization
S_milstein = milstein_discretization(S0, r, sigma, dt, N)

# Plotting the results
plt.figure(figsize=(14, 7))

# Plot for Euler discretization
plt.subplot(1, 2, 1)
plt.plot(t, S_euler, label='Euler Discretization')
plt.xlabel('Time t')
plt.ylabel('S(t)')
plt.title('Euler Discretization of Geometric Brownian Motion')
plt.legend()

# Plot for Milstein discretization
plt.subplot(1, 2, 2)
plt.plot(t, S_milstein, label='Milstein Discretization')
plt.xlabel('Time t')
plt.ylabel('S(t)')
plt.title('Milstein Discretization of Geometric Brownian Motion')
plt.legend()

plt.tight_layout()
plt.show()

# Return the last values for further steps if needed
(S_euler, S_milstein)
