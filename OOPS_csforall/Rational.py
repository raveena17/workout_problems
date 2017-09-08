class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def add(self, other):
        newNumerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        newDenominator = self.denominator*other.denominator
        return Rational(newNumerator, newDenominator)







#>>> r1=Rational(1,2)
#>>> r2=Rational(1,3)
#>>> r3=r1.add(r2)
#>>> r3.numerator
# 5
#>>> r3.denominator
# 6
