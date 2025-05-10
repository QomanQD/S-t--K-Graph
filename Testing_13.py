import numpy as np
import matplotlib.pyplot as plt

S0_45 = 45
S0_50 = 50
S0_55 = 55
K1 = 50
K2 = 55
mu = 0.07
sigma = 0.2
T = 6 / 12
N = 200
M = 10000
dt = T / N

def simulate(S0, mu, sigma, T, N, M):
    S = np.zeros((M, N+1))
    S[:, 0] = S0
    for i in range(1, N+1):
        Z = np.random.randn(M)
        S[:, i] = S[:, i-1] * (1 + mu * dt + sigma * np.sqrt(dt) * Z)
    return S

S1 =simulate(S0_45, mu, sigma, T, N, M)
S2 = simulate(S0_50, mu, sigma, T, N, M)
S3 = simulate(S0_55, mu, sigma, T, N, M)

final_prices_45 = S1[:, -1]
final_prices_50 = S2[:, -1]
final_prices_55 =S3[:, -1]

payoffs_45 = np.maximum(final_prices_45 - K1, 0)
payoffs_50 = np.maximum(final_prices_50 - K1, 0)
payoffs_55 = np.maximum(final_prices_55 - K2, 0)

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.hist(payoffs_45, bins=50, color='blue', alpha=0.7)
plt.title('Histogram of Payoffs for S0=45, K=50')
plt.xlabel('Payoff')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(payoffs_50, bins=50, color='orange', alpha=0.7)
plt.title('Histogram of Payoffs for S0=50, K=50')
plt.xlabel('Payoff')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(payoffs_55, bins=50, color='green', alpha=0.7)
plt.title('Histogram of Payoffs for S0=55, K=55')
plt.xlabel('Payoff')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()