import numpy as np
from scipy.integrate import quad



def phi(x):
    integrand = lambda t: (1 / np.sqrt(2 * np.pi)) * np.exp(-t**2 / 2)
    result, _ = quad(integrand, -np.inf, x)
    return result


def Scholes(S, K, T, mu, sigma):
    d1 = (np.log(S / K) + (mu + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    term1 = (S / 2) * (1 - phi(-d1 / np.sqrt(2)))
    term2 = (K / 2) * np.exp(-mu * T) * (1 - phi(-d2 / np.sqrt(2)))
    
    return term1 - term2


K = 50
mu = 0.07
sigma = 0.2
T = 0.5


price_50 = Scholes(50, K, T, mu, sigma)
price_55 = Scholes(55, K, T, mu, sigma)

print(f"C(S=50) = ${price_50:.4f}")
print(f"C(S=55) = ${price_55:.4f}")