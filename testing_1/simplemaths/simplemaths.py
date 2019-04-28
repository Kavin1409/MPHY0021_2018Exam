class SimpleMaths():
    '''
    A simple class to allow calculations to be performed on an integer.
    '''
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("argument must be an integer")
        self.number = number

    def square(self):
        return self.number ** 2

    def _factorial(self, value):
        if value == 0:
            return 1
        else:
            return value * self._factorial(value - 1)

    def factorial(self):
        if self.number < 0:
            raise ValueError("factorial not defined for negative values")
        return self._factorial(self.number)

    def power(self, power=3):
        return self.number ** power

    def oddOrEven(self):
        '''
        Note that this code assumes that 0 is even.
        '''
        if (self.number % 2) == 0:
            return 'Even'
        elif (self.number % 2) == 1:
            return 'Odd'

    def squareRoot(self):
        return self.number ** (0.5)
