import numpy as np
import matplotlib.pyplot as plt

S0=40
mu=0.05
sigma=0.2
T=1.0
N=252
dt=T/N

S=np.zeros(N)
S[0]=S0

np.random.seed(0)
epsilon=np.random.randn(N)

for n in range(1,N):
    S[n]=S[n-1]+mu*S[n-1]*dt+sigma*S[n-1]*epsilon[n]*np.sqrt(dt)

plt.figure(figsize=(10,5))
plt.plot(np.linspace(0,T,N),S,label='Simulated Stock Price')
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price')
plt.title('Stock Price Trajectory')
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()