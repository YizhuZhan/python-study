# -*- coding:utf-8 -*-
'''
    装饰器的作用（1）：封装;  (2)代码复用
'''

def my_sum_1(*args):
    if len(args) == 0:
        return 0
    for val in args:
        if not isinstance(val, int):
            return 0
    return sum(args)


def my_average_1(*args):
    if len(args) == 0:
        return 0
    for val in args:
        if not isinstance(val, int):
            return 0
    return sum(args) / len(args)


print(my_sum_1(1, 2, 3, 4, 5))
print(my_average_1(1, 2, 3, 4, 5))

print(my_sum_1(1, 2, 3, 4, 5, '6'))
print(my_average_1())
print('=' * 60)


# 把上面的公共部分提取出来做封装（闭包in_deco），放在装饰器函数中（deco）
def deco(f):
    def in_deco(*args):
        print('call deco')
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return f(*args)
    print('in_deco')
    return in_deco


def my_sum_2(*args):
    print('call sum2')
    return sum(args)


def my_average_2(*args):
    print('call average2')
    return sum(args) / len(args)

print(my_sum_2)
print(my_average_2)
# 被装饰函数标识符指向返回的函数对象
my_sum_2 = deco(my_sum_2)
my_average_2 = deco(my_average_2)
print(my_sum_2)
print(my_average_2)
print(my_sum_2(1, 2, 3, 4, 5))
print(my_average_2(1, 2, 3, 4, 5))
print(my_sum_2(1, 2, 3, 4, 5, '6'))
print(my_average_2())
print('=' * 60)


# 利用装饰器语法糖简写
@deco
def my_sum_3(*args):
    print('call sum3')
    return sum(args)


@deco
def my_average_3(*args):
    print('call average3')
    return sum(args) / len(args)


print(my_sum_3(1, 2, 3, 4, 5))
print(my_average_3(1, 2, 3, 4, 5))
print(my_sum_3(1, 2, 3, 4, 5, '6'))
print(my_average_3())


print(my_sum_3)
print(my_average_3)