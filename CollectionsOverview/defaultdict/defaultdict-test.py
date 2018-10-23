# -*-coding=utf-8 -*-
__author__ = 'Ivana'
from collections import defaultdict


users=["Ivana1", "Ivana2", "Ivana3", "Ivana1", "Ivana2", "Ivana2"]


# 方法一
user_dict1 = {}
for user in users:
    if user in user_dict1:
        user_dict1[user] += 1
    else:
        user_dict1[user] = 1
print(user_dict1)  # {'Ivana1': 2, 'Ivana2': 3, 'Ivana3': 1}


# 方法二
user_dict2 = {}
for user in users:
    user_dict2.setdefault(user, 0)
    user_dict2[user] += 1
print(user_dict2)  # {'Ivana1': 2, 'Ivana2': 3, 'Ivana3': 1}


# 方法三
user_dict3 = defaultdict(int)
for user in users:
    user_dict3[user] += 1
print(user_dict3)  # defaultdict(<class 'int'>, {'Ivana1': 2, 'Ivana2': 3, 'Ivana3': 1})


# 向defaultdict中传入自定义可调用对象
def gen_default():
    return {
        'name':'',
        'num': 0
    }

mydict = defaultdict(gen_default)
mydict["group1"]
print(mydict)  # defaultdict(<function gen_default at 0x0000000004EA4C80>, {'group1': {'name': '', 'num': 0}})