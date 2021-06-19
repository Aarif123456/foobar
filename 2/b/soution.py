from operator import attrgetter
class Elevator():
    def __init__(self, version):
        s = version.split(".")
        self.major=self.minor=self.rev=-1
        if len(s)>0: self.major = int(s[0])
        if len(s)>1: self.minor = int(s[1])
        if len(s)>2: self.rev = int(s[2])
        self.version = version

    def __repr__(self):
        return self.version

        
def solution(xs):
    ele = [Elevator(s) for s in xs]
    ele = sorted(ele, key=attrgetter('major', 'minor', 'rev'))
    return [str(e) for e in ele]

# Your code here
###############################################
# Code below is not submitted
import unittest

class sTest(unittest.TestCase):

    def test_function(self):
        test_cases = \
            [
               (["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"], ["0.1","1.1.1","1.2","1.2.1","1.11","2","2.0","2.0.0"]),\
               (["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]),\
               (["1", "1.0.0", "1.0"],["1", "1.0", "1.0.0"]),\
               (["5","4","3"],["3","4","5"]),\
               (["1.0"],["1.0"]),\
               (["1"],["1"]),\
               (["1.0.0"],["1.0.0"]),\
               (["0.39","0.48","0.0.99"],["0.0.99","0.39","0.48"]),\
               ([],[]),\
            ]
        for arguments, expected in test_cases:
            with self.subTest(arguments=arguments, expected=expected):
                self.assertEqual(solution(arguments), expected)


if __name__ == '__main__':
    unittest.main()


    