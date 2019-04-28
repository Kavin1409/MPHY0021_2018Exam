import pytest as pt
from simplemaths.simplemaths import SimpleMaths as sm


def approx(a,b):
    '''
    checks that percentage error of b to a is lower than 0.01
    '''
    if isinstance(a, complex) and isinstance(b, complex):
        check_real = approx(a.real, b.real)
        check_imag = approx(a.imag, b.imag)
        return check_real and check_imag
    else:
        return abs(a - b) <= 0.01 * a


class TestSimpleMaths():
    '''
    runs a series of positive and negative tests for the SimpleMaths class
    contains both positive ('Pos') and negative ('Neg') tests
    '''
    def testConstructorNeg(self):
        with pt.raises(TypeError) as exception:
            sm(2.0)
                 
    def testConstructorPos(self):
        all_matches = True
        value_arr = [1,5,7,2, -3]
        for val in value_arr:
            # can use self. number defined in __init__ to get back the same value!
            check = val == sm(val).number
            if not check:
                all_matches = False
        assert all_matches
    
    def testSquare(self):
        all_matches = True
        inputs = [4, 6, -5, 10]
        results = [16, 36, 25, 100]
        for inp, result in zip(inputs, results):
            check = result == sm(inp).square()
            if not check:
                all_matches = False
        assert all_matches
    
    def testFactorialPos(self):
        all_matches = True
        inputs = [4, 6, 0, 10]
        results = [24, 720, 1, 3628800]
        for inp, result in zip(inputs, results):
            check = result == sm(inp).factorial()
            if not check:
                all_matches = False
        assert all_matches
        
    def testFactorialNeg(self):
        with pt.raises(ValueError) as exception:
            sm(-5).factorial()
    
    def testPower(self):
        all_matches = True
        input_pairs = [[4, 0], [4, 2.5], [0, 5], [10,-2], [3, None]]
        results = [1, 32, 0, 0.01, 27]
        for pair, result in zip(input_pairs, results):
            if pair[1] is not None:
                check = approx(result, sm(pair[0]).power(pair[1]))
            else:
                check = approx(result, sm(pair[0]).power())
            if not check:
                all_matches = False
        assert all_matches
    
    def testOddOrEven(self):
        all_matches = True
        inputs = [3, 13, 58, 10]
        results = ['Odd', 'Odd', 'Even', 'Even']
        for inp, result in zip(inputs, results):
            check = result == sm(inp).oddOrEven()
            if not check:
                all_matches = False
        assert all_matches
    
    def testSquareRootPos(self):
        all_matches = True
        inputs = [4, 6, 9, 10, -3]
        results = [2, 2.45, 3, 3.16, (1.06e-16+1.73j)]
        for inp, result in zip(inputs, results):
            check = approx(result, sm(inp).squareRoot())
            if not check:
                all_matches = False
        assert all_matches
