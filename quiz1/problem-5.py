def isPrime(x):
    isPr = True
    for i in range(2,x):
        if x % i == 0:
            isPr = False
    return isPr


def primesList(N):
    primes = []
    for i in range(2,N+1):
        if isPrime(i):
            primes.append(i)
    return primes

print primesList(10)
