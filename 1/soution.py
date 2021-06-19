import math
def findLargest(num, limit):
    for m in range(limit, 0, -1):
        if num>= m*m: return m
    return 1

def solution(area):
    upper_limit = 1000
    out = []
    while area>0:
        n = findLargest(area,upper_limit)
        num = n*n
        out.append(num)
        area-= num
        upper_limit = n
    return out

###############################################
# Code below is not submitted
import unittest
    
class sTest(unittest.TestCase):

    def test_function(self):
        test_cases = \
            [
                (15324, [15129,169,25,1]),\
                (12, [9,1,1,1]),\
                (1, [1]),\
                (4, [4]),\
                (5, [4,1]),\
                (85, [81, 4]),\
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(solution(arguments), expected)


if __name__ == '__main__':
    unittest.main()


