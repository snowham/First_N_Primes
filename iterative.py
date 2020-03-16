def firstNPrimesIterative(N):
    primes = [2]
    maybePrime = 3
    while len(primes) < N:
        ptest = [maybePrime for i in primes if maybePrime%i == 0]
        primes += [] if ptest else [maybePrime]
        maybePrime += 2
    return primes

n = 10
first_n_primes = firstNPrimesIterative(n)
print(first_n_primes)
