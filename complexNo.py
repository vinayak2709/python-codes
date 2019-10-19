import math


class Complex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, no):
        NewReal = self.real + no.real
        NewImag = self.imaginary + no.imaginary
        return Complex(NewReal, NewImag)

    def sub(self, no):
        NewReal = self.real - no.real
        NewImag = self.imaginary - no.imaginary
        return Complex(NewReal, NewImag)

    def mul(self, no):
        NewReal = self.real * no.real - self.imaginary * no.imaginary
        NewImag = self.imaginary * no.real + self.real * no.imaginary
        return Complex(NewReal, NewImag)

    def truediv(self, no):
        mag1 = math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
        angle1 = math.atan(self.imaginary / self.real)
        mag2 = math.sqrt(no.real * no.real + no.imaginary * no.imaginary)
        angle2 = math.atan(no.imaginary / no.real)

        NewMag = mag1 / mag2
        NewAngle = angle1 - angle2

        NewReal = NewMag * math.cos(NewAngle)
        NewImag = NewMag * math.sin(NewAngle)
        return Complex(NewReal, NewImag)

    def mod(self):
        mag1 = math.sqrt(self.real * self.real + self.imaginary * self.imaginary)
        img = 0.00
        return Complex(mag1, img)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


#if __name__ == '__main__':
print(Complex(2,1).mod())
print(Complex(3,2).mod())
a=Complex(2,1)
b=Complex(3,2)

print(a.add(b))
print(a.sub(b))
print(a.mul(b))
print(a.truediv(b))


