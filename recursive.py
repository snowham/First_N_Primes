import numpy as np
import sys
sys.setrecursionlimit(10000)

def firstNPrimesRecursive(n):
    primes = np.array([])
    if n == 1:
        primes = np.append(primes, 2)
    elif n == 2:
        primes = np.append(primes, [2, 3])
    else:
        primes = firstNPrimesRecursive(n-1)
        maybePrime = primes[-1] + 2
        isPrime = False
        while not isPrime:
            if True in (maybePrime%primes == 0):
                maybePrime += 2
                continue
            else:
                primes = np.append(primes, maybePrime)
                isPrime = True
    return primes

n = 10
first_n_primes = firstNPrimesRecursive(n).tolist()
for idx, val in enumerate(first_n_primes):
    first_n_primes[idx] = int(val)
print(first_n_primes)
