# 1: formNumberFromOddDigits()
# solution with string:
# def formNumberFromOddDigits(n):
#     newNum = ''
#     sign = n // abs(n)
#     if sign == 1:
#         n = str(n)
#     elif sign == -1:
#         n = str(n)[1:]
#     for digit in n:
#         if digit in '13579':
#             newNum += digit
#     if newNum == '':
#         return 0
#     else:
#         return sign * int(newNum)

# solution without string:
def formNumberFromOddDigits(n):
    newNum = 0
    sign = n // abs(n)
    n = abs(n)
    currDigit = 0
    while n > 0:
        digit = n % 10
        n //= 10
        if digit in [1, 3, 5, 7, 9]:
            newNum += digit * 10 ** currDigit
            currDigit += 1
    return newNum * sign

# 2: nthPalindromicPrime()
def nthPalindromicPrime(n):
    guess = -1
    found = -1
    while found < n:
        guess += 1
        if isPalindromicPrime(guess):
            found += 1
    return guess

def isPalindromicPrime(n):
    return isPrime(n) and isPalindromic(n)  

import math

def isPrime(n):
    if n < 2: return False
    elif n == 2: return True
    else:
        cap = math.ceil(n ** .5)
        for i in range(2, cap + 1):
            if n % i == 0:
                return False
        return True

# solution with string:
# def isPalindromic(n):
#     return str(n) == str(n)[::-1]

# solution without string:
def isPalindromic(n):
    return n == reverse(n)

def reverse(n):
    # works only with Z+
    hiPow = digitCount(n) - 1
    rev = 0
    depth = 0
    while n > 0:
        thisDigit = n % 10
        n //= 10
        rev += thisDigit * 10 ** (hiPow - depth)
        depth += 1
    return rev

def digitCount(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# ignore_rest

def testFormNumberFromOddDigits():
    print('Testing formNumberFromOddDigits()...', end='')
    assert(formNumberFromOddDigits(9421)==91)
    assert(formNumberFromOddDigits(-1648)==-1)
    assert(formNumberFromOddDigits(60248)==0)
    assert(formNumberFromOddDigits(-20)==0)
    assert(formNumberFromOddDigits(-11321)==-1131)
    print('Passed!')

def testReverse():
    print('Testing reverse()...', end='')
    assert(reverse(654312987)==789213456)
    assert(reverse(100023)==320001)
    assert(reverse(2000)==2)
    assert(reverse(86031)==13068)
    assert(reverse(5)==5)
    print('Passed!')

def testIsPrime():
    print('Testing isPrime()...', end='')
    primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107,
        109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193,
        197, 199])
    for num in range(200):
        if num in primes:
            assert(isPrime(num))
        else:
            assert(not isPrime(num))
    print('Passed!')

def testIsPalindromicPrime():
    print('Testing isPalindromicPrime()...', end='')
    pp = set([2, 3, 5, 7, 11, 101, 131, 151, 181,
        191, 313, 353, 373, 383, 727, 757, 787,
        797, 919, 929])
    for i in range(1000):
        if i in pp:
            assert(isPalindromicPrime(i))
        else:
            assert(not isPalindromicPrime(i))
    print('Passed!')

def testAll():
    testFormNumberFromOddDigits()
    testReverse()
    testIsPrime()
    testIsPalindromicPrime()

def main():
    testAll()

if __name__ == '__main__':
    main()
