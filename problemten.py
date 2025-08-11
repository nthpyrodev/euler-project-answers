# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

number = 20000000

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sumOfPrimes(n):
    primes = 0
    for i in range(2,n):
        if isPrime(i):
            primes += i
    return primes

print(sumOfPrimes(number))