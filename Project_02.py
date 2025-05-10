import numpy as np

mu=0.07
T=1/2
N=200
dt=T/N
M=10000
sigma=0.2

def f(S):
    K=50
    return max(S-K,0)

S_N=np.zeros(M)
for i in range(M):
    S=np.zeros(N)
    S[0]=45
    np.random.seed(5)
    epsilon=np.random.randn(N)

    for n in range(1,N):
         S[n]=S[n-1]+mu*S[n-1]*dt+sigma*S[n-1]*epsilon[n]*np.sqrt(dt)

         S_N[i]=S[-1]


mp=np.mean([f(S_n)for S_n in S_N])
c=(1+mu*dt)**-N*mp

print(f"Value of C: {c}")
