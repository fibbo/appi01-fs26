class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __str__(self):
        return (
            f"{self.real} {'+' if self.imaginary >= 0 else '-'} {abs(self.imaginary)}j"
        )


a = Complex(2, 3)
b = Complex(1, -5)

print(a + b)
