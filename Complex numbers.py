class Complex:
    def __init__(self, re=0, im=0):
        if ((isinstance(re, float) or isinstance(re, int)) and
                (isinstance(im, float) or isinstance(im, int))):
            self.re = re
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        return f"{self.re}{self.im:+}i"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (float, int)):
            return Complex(self.re + other, self.im)
        else:
            raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (float, int)):
            return Complex(self.re - other, self.im)
        else:
            raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.im * other.im,
                           self.im * other.re + self.re * other.im)
        elif isinstance(other, (float, int)):
            return Complex(self.re * other, self.im * other)
        else:
            raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self.re * other.re + self.im * other.im) /
                           (other.re ** 2 + other.im ** 2),
                           (self.im * other.re - self.re * other.im) /
                           (other.re ** 2 + other.im ** 2))
        elif isinstance(other, (float, int)):
            return Complex(self.re / other, self.im / other)
        else:
            raise TypeError()

    def __eq__(self, other):
        if isinstance(other, Complex):
            if self.re == other.re and self.im == other.im:
                return True
            else:
                return False
        elif isinstance(other, (float, int)):
            if self.im == 0 and self.re == other:
                return True
            else:
                return False
        else:
            raise TypeError()

    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5
