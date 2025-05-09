import numpy as np
import matplotlib.pyplot as plt    

K=50
S=np.linspace(0,100,500)

payoff =np.maximum(S-K,0)

plt.figure(figsize=(8,5))
plt.plot(S, payoff, label='Call Option Payoff', color='blue')
plt.axvline(x=K,linestyle='--',color='red',label='Strike Price')
plt.axhline(y=0,color='black',linewidth=0.8)
plt.axvline(x=0,color='black',linewidth=0.8)
plt.title('European Call Option Payoff')
plt.xlabel('Stock Price')
plt.ylabel('Payoff')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()