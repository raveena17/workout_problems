class Arithmetic:
  
    def __init__(self, x, y):
        self.n = x
        self.d = y

    def __add__(self, other):
        if not isinstance(other, Arithmetic):
            other = Arithmetic(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return Arithmetic(n, d)

    def __sub__(self, other):
        if not isinstance(other, Arithmetic):
            other = Arithmetic(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return Arithmetic(n1*d2 - n2*d1, d1*d2)

    def __mul__(self, other):
        if not isinstance(other, Arithmetic):
            other = Arithmetic(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return Arithmetic(n1*n2, d1*d2)

    def __div__(self, other):
        if not isinstance(other, Arithmetic):
            other = Arithmetic(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return Arithmetic(n1*d2, d1*n2)

    
