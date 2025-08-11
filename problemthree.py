# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

exampleNumber = 600851475143
largestFactor = 0

def largestPrimeFactor(n):
    while n % 2 == 0:
        largestFactor = 2
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largestFactor = i
            n = n // i

    if n > 2:
        largestFactor = n

    return largestFactor

print(largestPrimeFactor(exampleNumber))