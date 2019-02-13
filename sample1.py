"""Name: Sarah Andert
    Course: CMPS 1500
    Lab Assignment
    Date: 11/12/2018
    Creating class Rational to practice overloading operators division, power, conversion to float

"""


from sys import *

class Rational:
    
    def __init__(self, n, d):
        if d == 0:
            print("Invalid Denominator!")
            sys.exit()  # import sys for this to work (ugly!)
        else:
            self.numerator = n
            self.denominator = d
            
    def __repr__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __str__(self):return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator* other.numerator

    def __truediv__(self, other):
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Rational(n,d)

    def __pow__(self, e):
        n = self.numerator ** e
        d = self.denominator ** e
        return Rational(n,d)

    def __float__(self):
        return self.numerator / self.denominator
            
