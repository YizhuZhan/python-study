# -*- coding:utf-8 -*-


class Fib(object):
    def __init__(self, num):
        self.fiblist = []
        firstnum = 0
        if num >= 1:
            self.fiblist.append(firstnum)
        secondnum = 1
        if num >= 2:
            self.fiblist.append(secondnum)
        if num >= 3:
            for i in range(2, num):
                tmpnum = secondnum
                secondnum += firstnum
                firstnum = tmpnum
                self.fiblist.append(secondnum)

    def __str__(self):
        return ','.join(map(lambda i: str(i), self.fiblist))

    def __len__(self):
        return len(self.fiblist)


f = Fib(10)
print(f)
print(len(f))


class Rational(object):

    def __init__(self, p, q):
        self.p = int(p)
        self.q = int(q)

    def __add__(self, r):
        upper = self.p * r.q + self.q * r.p
        lower = self.q * r.q
        d = gcd(upper, lower)
        upper /= d
        lower /= d
        return Rational(upper, lower)

    def __sub__(self, r):
        upper = self.p * r.q - self.q * r.p
        lower = self.q * r.q
        d = gcd(upper, lower)
        upper /= d
        lower /= d
        return Rational(upper, lower)

    def __mul__(self, r):
        upper = self.p * r.p
        lower = self.q * r.q
        d = gcd(upper, lower)
        upper /= d
        lower /= d
        return Rational(upper, lower)

    # python2中为__div__, python3中为__truediv__
    def __truediv__(self, r):
        upper = self.p * r.q
        lower = self.q * r.p
        d = gcd(upper, lower)
        upper /= d
        lower /= d
        return Rational(upper, lower)

    def __str__(self):
        if self.q != 1:
            return "%d/%d" % (self.p, self.q)
        else:
            return str(self.p)

    __repr__ = __str__


def gcd(m, n):
    return m if n == 0 else gcd(n, m%n)


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)


class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q


print(int(Rational(7, 2)))
print(float(Rational(7, 2)))
print(int(Rational(1, 3)))
print(float(Rational(1, 3)))
