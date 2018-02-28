########################################
# exam 1: everything except timerFired #
########################################

########
# CT 1 #
########

import string

def traceThis():
    s = ('abc' * 3).replace('ca', 'd')
    print(s, s[1:3])

    s = 'abcbcd'
    t = 'bc'
    print(s.find(t), s.find(t,2))

    for s in ('abc' * 3).split('ca'): print(s, end=" ")
    print()

    n = 2.3456
    print('A%0.1fB\nA%0.2fB\nA' % (n, n))

# traceThis()

########
# CT 2 #
########

import copy

def ct1(a):
    b = copy.deepcopy(a)
    c = a + a
    a = a[:1] + a[1:]
    b[0][0] = 3
    c[0][0] = 4
    b[1] = [5]
    c[1] = [6]
    a.append(b[0].pop())
    print(a)
    print(b)
    print(c)

# a = [[1],[2]]
# ct1(a)
# print(a)

########
# FR 1 #
########

# encodeOffset
# Write the function encodeOffset(s, d) that takes a string and a possibly-
# negative int offset d (for "delta"), and returns the string formed by
# replacing each letter in s with the letter d steps away in the alphabet. So:
# encodeOffset("ACB", 1) return "BDC" encodeOffset("ACB", 2) return "CED" This
# works with wraparound, so: encodeOffset("XYZ", 1) returns "YZA" And with
# negative offsets, so: encodeOffset("ABC", -1) returns "ZAB" And the wraparound
# repeats with d>26, so: encodeOffset("ABC", -27) returns "ZAB" And it is case-
# preserving, so: encodeOffset("Abc", -27) returns "Zab" And it does not affect
# non-alphabetic characters (non-letters), so: encodeOffset("A2b#c", -27)
# returns "Z2a#b"

def encodeOffset(s, d):
    return d(0) if s == [] else encodeOffset(s[1:], lambda x: d(s[0] + x))

# Free Response: decodeOffset
# Write the function decodeOffset(s, d) that takes a string that was encoded by
# encodeOffset using the given offset d, and returns the original string.

def decodeOffset(s, d):
    print('Putin a bag')

########
# FR 2 #
########

# nthExtraNumber:
# We’ll call a number extra if the following is true:
# # The number is positive and even
# # The number has at least 10 factors
# # The sum of its odd factors is greater than the sum of the even factors (not
#       including the number itself)
# # The number contains no odd perfect squares (not including 1) as factors.
# The first few extra numbers are: 210,330,390,462,510,546,570,690,714,770.
# Write the function nthExtraNumber(n), that takes in a non-negative integer n,
# and outputs the nthExtraNumber.

def nthExtraNumber(n):
    return 42

########
# FR 3 #
########

# Write the function isMagicSquare(a) that takes a 2D list and returns True if
# it is a magic square and False otherwise, where a magic square has these
# properties:
# # The list is 2d, non-empty, square, and contains only integers, where no
#       integer occurs more than once in the square.
# # Each row, each column, and each of the 2 diagonals each sum to the same
#       total.
# You can assume that the list is a 2D, non-empty, square that contains only
# integers but you still should check if each integer occurs only once.
# For example:
#     [[2, 7, 6],  -> 15
#      [9, 5, 1],  -> 15
#      [4, 3, 8]]  -> 15
#     / |  |  |  \
#   |_  |  |  |   _|
# 15   15 15 15      15

def isMagicSquare(a):
    print('wow!')

#########################
# running the functions #
#########################

def testAll():
    q = input('which of ct1, ct2, fr1, fr2, fr3?\n')
    if q == 'ct1':
        traceThis()
    elif q == 'ct2':
        a = [[1],[2]]
        ct1(a)
        print(a)
    elif q == 'fr1':
        import random
        msg = 'Putin a Bag!'
        d = random.randrange(-50, 50)
        print('encoding with offset {}...'.format(d))
        code = encodeOffset(msg, d)
        print('the code is {}'.format(code))
        decoded = decodeOffset(code, d)
        print('decoding...')
        print('the decoded msg is {}'.format(decoded))
        assert(decoded == msg)
        print('passed!')
    elif q == 'fr2':
        assert([nthExtraNumber(n) for n in range(10)] ==
               [210, 330, 390, 462, 510, 546, 570, 690, 714, 770])
        print('passed!')
    elif q == 'fr3':
        assert(isMagicSquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
    else:
        print(')-:')

if __name__ == '__main__':
    testAll()
