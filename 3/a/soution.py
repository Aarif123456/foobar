from fractions import Fraction
import math
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
    
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def get_identity_matrix(size):
    return [[1 if i==j else 0 for i in range(size)] for j in range(size)]

def subtract_matrices(X, Y):
    assert(len(X) == len(Y))
    if len(X[0])==0: return []
    assert(len(X[0]) == len(Y[0]))
    return [[X[i][j]-Y[i][j] for i in range(len(X))] for j in range(len(X[0]))]

def create_probability_matrix(matrix):
    out = []
    for row in matrix:
        n = sum(row)
        out.append([Fraction(0) if n==0 else Fraction(i,n) for i in row])
    return out

def get_lcm(arr):
    denominators = [Fraction(r).denominator for r in arr]
    lcm = denominators[0]
    for d in denominators[1:]:
        lcm = lcm // gcd(lcm, d) * d

    return lcm

# Given v find w where w=v(I−A)^-1. 
def solution(xs):
    size = len(xs)
    terminal_list = get_terminal_list(xs)
    I = get_identity_matrix(size)
    A = create_probability_matrix(xs)
    w = subtract_matrices(I, A)
    w = inverse(w)
    w = [v[0] for v in w]
    terminal_fracs = []
    for i in range(size):
        if terminal_list[i]:
            terminal_fracs.append(w[i])
    d = Fraction(get_lcm(terminal_fracs))
    out = [ (frac * d).numerator for frac in terminal_fracs]
    out.append(d.numerator)
    return out
    
def get_terminal_list(matrix): 
    return [row.count(0) == len(row) for row in matrix]

def get_terminal_count(terminal): 
    return terminal.count(True)

# Your code here
###############################################
# Code below is not submitted
import unittest

class sTest(unittest.TestCase):
    def test_identitity(self):
        test_cases = \
            [
               (2,[[1,0],[0,1]]),\
               (4,[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(get_identity_matrix(arguments), expected)

    def test_terminal_count(self):
        test_cases = \
            [
               ([[1,0,2,-1],\
                [0,0,0,0],\
                [0,0,0,0],\
                [1,0,5,0],\
               ],2),\
               ([[1,1],\
                [0,0],\
                [0,0],\
                [0,0],\
               ],3)
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(get_terminal_count(get_terminal_list(arguments)), expected)

    def test_function(self):
        test_cases = \
            [
               ([
                   [0,1,1,0],\
                   [1,0,0,1],\
                   [0,0,0,0],\
                   [0,0,0,0],\
               ],[2,1,3]),\
               ([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]],[7, 6, 8, 21]),\
               ([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],[0, 3, 2, 9, 14])
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(solution(arguments), expected)


if __name__ == '__main__':
    unittest.main()

