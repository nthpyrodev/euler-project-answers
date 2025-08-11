# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


found = False

for a in range(1,500):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            found = True
            print(f"Triplet: a = {a}, b = {b}, c = {c}")
            print(f"Product abc = {a * b * c}")
            break
    if found:
        break