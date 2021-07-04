def solution(n):
    coefficients = [1]+[0]*n
    for i in range(1, n+1):
        for j in range(n, i-1, -1):
            coefficients[j] += coefficients[j-i]
    return coefficients[n]-1 

# Your code here
###############################################
# Code below is not submitted
import unittest

class sTest(unittest.TestCase):

    def test_function(self):
        test_cases = \
            [
               (1,0), 
               (2,0),# Start adding by 1
               (3,1),
               (4,1),
               (5,2),
               (6,3),
               (7,4),
               (8,5),# Start adding by 2
               (9,7),
               (10,9),
               (11,11),# Start adding by 3
               (12,14),
               (13,17),# Start adding by 4
               (14,21),# Start adding by 5
               (15,26),
               (16,31),# Start adding by 6
               (17,37),# Start adding by 8
               (18,45),
               (19,53),
               (20,63),
               (21,75),
               (22,88),
               (23,103),
               (24,121),
               (25,141),
               (200,487067745)
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(solution(arguments), expected)


if __name__ == '__main__':
    unittest.main()

