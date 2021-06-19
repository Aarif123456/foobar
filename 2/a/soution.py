def solution(xs):
    if len(xs) == 1: return str(xs[0])
    ans = 1
    smallestAbsMin = 100001
    zeroCount = 0
    oddNegatives = False
    # Every negative number needs a pair 
    # We remove the negative number with a smaller magnitude
    for n in xs:
        if n==0: 
            zeroCount+=1
            continue
        if n<0:
            smallestAbsMin = min(abs(n), smallestAbsMin);
            oddNegatives = not oddNegatives;
        ans *= abs(n)
    # possible leftover negative
    bne = int(smallestAbsMin)
    ans = int(ans)
    if zeroCount == len(xs) or (zeroCount+1 == len(xs) and ans==bne): return "0"
    if oddNegatives: ans/=bne
    return str(int(ans))

# Your code here
###############################################
# Code below is not submitted
import unittest

class sTest(unittest.TestCase):

    def test_function(self):
        test_cases = \
            [
               ([2, 0, 2, 2, 0],"8"),\
               ([-2, -3, 4, -5],"60"),\
               ([2, -3, 4, -5],"120"),\
               ([0,0,0],"0"),\
               ([0,0,-1],"0"),\
                ([-1],"-1"),\
                ([-12, -12, 2, 0, 0, 0,0,0,0],"288"),\
               ([0, -123,0,-12],"1476"),\
               ([0, -123,0,-12, -1, -13, 2],"38376"),\
               ([0, 1, -2, 0],"1")
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(solution(arguments), expected)


if __name__ == '__main__':
    unittest.main()


    