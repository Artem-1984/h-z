class Circle:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x is other.x

    def __gt__(self, other):
        return self.x > other.x

    def __it__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x <= other.x

    def __ge__(self, other):
        return self.x >= other.x

    def __add__(self, other):
        new = self.x + other.x
        return new

    def __sub__(self, other):
        new1 = self.x - other.x
        return new1

    def __iadd__(self, other):
        self.x += other.x
        return self

    def __isub__(self, other):
        self.x -= other.x
        return self


c1 = Circle(222)
c2 = Circle(14)
print(c1 == c2)
print(c1 < c2)
print(c1 > c2)
print(c1 >= c2)
print(c1 <= c2)
print((c1 >= c2))
print(c1 + c2)
print(c1 - c2)
print(c1 + c2)
print(c1 - c2)


class Complex:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        n = complex(self.x, other.x)
        return n

    def __mul__(self, other):
        n1 = complex(self.x * other.x)
        return n1

    def __sub__(self, other):
        n2 = complex(self.x - other.x)
        return n2

    def __truediv__(self, other):
        n3 = complex(self.x / other.x)
        return n3


c = Complex(3 + 2.2j)
c1 = Complex(5 + 1.8j)
print(c + c1)
print(c * c1)
print(c - c1)
print(c / c1)


class Airplane:
    def __init__(self, type, passenger, max_p):
        self.type = type
        self.passenger = passenger
        self.max_p = max_p

    def __eq__(self, other):
        n = self.type == other.type
        return n

    def __add__(self, other):
        return self.passenger + 10

    def __sub__(self, other):
        return self.passenger - 10

    def __iadd__(self, other):
        self.passenger += other.passenger
        return self.passenger

    def __isub__(self, other):
        other.passenger -= self.passenger

    def __it__(self, other):
        return other.max_p

    def __le__(self, other):
        return other.max_p

    def __gt__(self, other):
        return self.max_p

    def __ge__(self, other):
        return self.max_p


a = Airplane('боенг', 55, 100)
a1 = Airplane('ил-2', 60, 95)
print(a == a1)
print(a.__add__(10))
print(a - 10)
print(a.passenger + a1.passenger)
print(a1.passenger - a.passenger)
print(a.max_p > a1.max_p)
print(a.max_p >= a1.max_p)
print(a.max_p <= a1.max_p)
print(a.max_p < a1.max_p)


class Flat:
    def __init__(self, apartment, price):
        self.apartment = apartment
        self.price = price

    def __eq__(self, other):
        return self.apartment == other.apartment

    def __ne__(self, other):
        return self.apartment != other.apartment

    def __it__(self, other):
        return other.price

    def __le__(self, other):
        return other.price

    def __gt__(self, other):
        return self.price

    def __ge__(self, other):
        return self.price


f = Flat(28.3, 2500000)
f1 = Flat(34.5, 30000000)
print(f == f1)
print(f != f1)
print(f.price < f1.price)
print(f.price <= f1.price)
print(f.price > f1.price)
print(f.price >= f1.price)
