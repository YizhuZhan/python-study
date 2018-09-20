# -*- coding:utf-8 -*-
import functools
import sys


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    # python2用，python3不再使用
    # def __cmp__(self, s):
    #     if not isinstance(s, Student):
    #         return -1
    #     elif self.score > s.score:
    #         return -1
    #     elif self.score < s.score:
    #         return 1
    #     elif self.name < s.name:
    #         return -1
    #     elif self.name > s.name:
    #         return 1
    #     else:
    #         return 0

    # python3中用__lt__, __gt__, __eq__, __le__, __ge__等代替__cmp__
    # If you use the functools.total_ordering decorator, you only need to implement e.g. the __lt__ and __eq__ methods
    @functools.total_ordering
    def __lt__(self, other):
        return (self.score > other.score) and ((self.score == other.score) or (self.name < other.name))

    def __eq__(self, other):
        return (self.score == other.score) and (self.name == other.name)

    # def __gt__(self, other):
    #     return (self.score < other.score) and ((self.score == other.score) or (self.name > other.name))


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print(sorted(L))


# a mixin definition
PY3 = sys.version_info[0] >= 3
if PY3:
    def cmp(a, b):
        return (a > b) - (a < b)

    # mixin class for Python3 supporting __cmp__
    class PY3__cmp__:

        def __eq__(self, other):
            return self.__cmp__(other) == 0

        def __ne__(self, other):
            return self.__cmp__(other) != 0

        def __gt__(self, other):
            return self.__cmp__(other) > 0

        def __lt__(self, other):
            return self.__cmp__(other) < 0

        def __ge__(self, other):
            return self.__cmp__(other) >= 0

        def __le__(self, other):
            return self.__cmp__(other) <= 0
else:
    class PY3__cmp__:
        pass


class Point(PY3__cmp__):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

    __repr__ = __str__

    def __cmp__(self, other):
        return -1 if self.x < other.x else 1 if self.x > other.x else -1 if self.y < other.y \
            else 1 if self.y > other.y else -1 if self.z < other.z else 1 if self.z > other.z else 0


p1 = Point(1, 2, 3)
p2 = Point(2, 2, 1)
p3 = Point(1, 3, 2)
p_list = [p1, p2, p3]
print(sorted(p_list))


class Fib(object):
    def __call__(self, num):
        first = 0
        second = 1
        fiblist = []
        fiblist.append(first)
        for i in range(num - 1):
            first, second = second, first + second
            fiblist.append(first)
        return fiblist

f = Fib()
f(10)
print(f(10))


