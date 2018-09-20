# -*- coding:utf-8 -*-
import math
import functools


def add(x, y, _f):
    return _f(x) + _f(y)
print(add(25, 9, math.sqrt))


def format_name(s):
    return s[0].upper() + s[1:].lower()
print(list(map(format_name, ['adam', 'LISA', 'barT'])))


def f(x, y):
    return x + y
print(functools.reduce(f, [1, 3, 5, 7, 9]))  # output: 25
print(functools.reduce(f, [1, 3, 5, 7, 9], 100))  # output: 125


def is_not_empty(s):
    return s and len(s.strip()) > 0
print(list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))  # output: ['test', 'str', 'END']


def is_sqr(x):
    return math.sqrt(x) % 1 == 0
print(list(filter(is_sqr, range(1, 101))))  # output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
