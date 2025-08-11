# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

for a in range(100,999):
    for b in range(100,999):
        palindrome = a * b
        reversePalindrome = int(str(palindrome)[::-1])
        if palindrome == reversePalindrome:
            largestPalindrome = palindrome
print(largestPalindrome)