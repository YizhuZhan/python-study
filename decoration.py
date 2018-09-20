# -*- coding:utf-8 -*-
import time
import functools
from functools import reduce


# 不带参数的decorator，两层嵌套
# def log(arg):
def performance(f):
    def fn(*args, **kw):
        start = time.time()
        r = f(*args, **kw)
        end = time.time()
        # print('call %s() in %fs...[%s]' % (f.__name__, end - start, arg))
        print('call %s() in %fs...' % (f.__name__, end - start))
        return r
    return fn
    # return performance


# @log("info")
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))


print(factorial(10))


#  带参数的decorator，三层嵌套，最外层用于传递装饰器参数
def deco(arg):  # 最外层函数定义的参数是=装饰函数的参数，该参数也可以是个类
    def _deco(func):  # 中间层函数定义的参数是=被装饰函数的名称
        def __deco(*args, **kwargs):  # 最内层函数定义的参数=传递给被装饰函数
            print('=' * 40)
            print("before %s called [%s]." % (func.__name__, arg))
            ret = func(*args, **kwargs)
            print(func)  # 打印被装饰函数的内存地址
            print("after %s called.[%s]." % (func.__name__, arg))
            return ret  # 返回被装饰函数的返回值
        return __deco  # 将最内层函数作为值返回
    return _deco  # 返回中间层函数


@deco("info")
def myfunc(a, b):
    print("myfunc(%s,%s) called" % (a, b))
    return a + b


@deco("debug")
def myfunc2(a, b, c):
    print("myfunc(%s,%s,%s) called." % (a, b, c))
    return a + b + c


myfunc(1, 4)
myfunc2(5, 6, 9)


# functools.wraps()的使用
def performance(unit):
    def f1(f):
        @functools.wraps(f)  # 用于把原函数的__name__、__doc__等信息复制到装饰器函数中，否则访问__name__会得到f2
        def f2(*args, **kw):
            t1 = time.time()
            print('call %s() in %s%s' % (f.__name__, t1, unit))
            return f(*args, **kw)
        return f2
    return f1


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial.__name__)
print(factorial(3))




