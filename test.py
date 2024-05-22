class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

def Complex_print(number):
    print(number.real, end='')
    if number.imaginary >= 0:
        print('+', end='')
    print(number.imaginary)

c1 = Complex(3.14, -1.7)
c2 = c1
c2.real = 2.72
Complex_print(c1)
Complex_print(c2)