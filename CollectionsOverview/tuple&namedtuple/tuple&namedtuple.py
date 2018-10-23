# -*-coding=utf-8 -*-
__author__ = 'Ivana'
from collections import namedtuple
# 抽象基类 interface
# from collections.abc import *
from collections import namedtuple


user_tuple = ('Ivana', 27, 167)
name, age, height = user_tuple
print(name, age, height)


name, *others = user_tuple
print(name, others)


user_info_dict = {}
user_info_dict[user_tuple] = 'programmer'
print(user_info_dict)


# namedtuple可以直接用于对接数据库读取结果
User = namedtuple("User", ["name", "age", "height"])
user1 = User("Ivana", 27, 167)
print(user1.name, user1.age, user1.height)
# namedtuple既可以按照字段名访问属性，也可以按照位置访问，从0开始
print(user1[0], user1[1], user1[2])
# 可以
print(user1)

# 取出数据库表user中的全部数据，并加入一列edu，使用namedtuple的user对象增加"edu"后可以直接对接数据库存入
# 单*参数
User = namedtuple("User", ["name", "age", "height", "edu"])
user_tuple = ("Ivana", 27, 167)
user2 = User(*user_tuple, "master")
print(user2.name, user2.age, user2.height, user2.edu)


# 双*参数
User = namedtuple("User", ["name", "age", "height", "edu"])
user_dict = {"name": "sql", "age": 27, "height": 178}
user3 = User(**user_dict, edu="master")
print(user3.name, user3.age, user3.height, user3.edu)


# 用namedtuple生成的类，实例化得到的对象实体支持拆包特性，而普通类对象不支持
name, age, *others = user3
print(name, age, others)


# namedtuple中的_asdict()方法:可将tuple转换成dict，并返回一个OrderdDict类的对象
d2 = user2._asdict()
print(d2)
userd2 = User(**d2)
print(userd2.name, userd2.age, userd2.height, userd2.edu)


# _make()方法放iteirable参数，但灵活性不高
try:
    user4 = User._make(['zyz', 18, 165])
except Exception as e:
    print(e.args)  # Expected 4 arguments, got 3
    user4 = User._make(['zyz', 18, 165, "master"])
finally:
    print(user4)  # User(name='zyz', age=18, height=165, edu='master')