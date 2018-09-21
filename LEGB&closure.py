# -*- coding:utf-8 -*-


# python解释器查找变量顺序：L > E > G > B
def get_pass_100(val):
    print('%x' % id(val))
    # local
    passline = 60
    if val >= passline:
        print("pass")
    else:
        print("fail")

    def in_func():  # (val, )
        print(val)
    in_func()
    # 返回函数名（函数对象入口地址）
    return in_func


def get_pass_150(val):
    print('%x' % id(val))
    # local
    passline = 90
    if val >= passline:
        print("pass")
    else:
        print("fail")

    def in_func():  # (val, )
        print(val)

    in_func()
    # 返回函数名（函数对象入口地址）
    return in_func

# global
passline = 80
f_100 = get_pass_100(70)
f_100()
# 函数f，即in_func的第一个参数地址和local变量val地址同
print(f_100.__closure__)

f_150 = get_pass_150(70)
f_150()
print(f_150.__closure__)


print("=" * 60)


# 为了减少上述代码量，把get_pass_100和get_pass_150合为一体，passline以参数形式传入
def set_total_score(passline):
    def get_pass(val):
        print('val: %x' % id(val))  # 立即数
        print('passline: %x' % id(passline))
        if val >= passline:
            print("pass")
        else:
            print("fail")
    return get_pass
f_100_60 = set_total_score(60)
f_150_90 = set_total_score(90)
print(f_100_60.__closure__)
f_100_60(70)
print(f_150_90.__closure__)
f_150_90(70)
