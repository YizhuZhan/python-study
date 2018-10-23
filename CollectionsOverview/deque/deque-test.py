# -*-coding=utf-8 -*-
__author__ = 'Ivana'
from collections import deque
import copy
#!/usr/bin/python
# import sys
# print(sys.version)
import platform
version = platform.python_version()
if version.startswith('2'):
# try:
    # python2
    from Queue import Queue
else:
    # python3
    from queue import Queue


# list从队尾弹出，无法操作队头
user_list = ["Ivana"]
user_name = user_list.pop()
print(user_name, user_list)  # Ivana []


# deque是双端队列
user_deque = deque()
# 队尾插入
user_deque.append("Ivana")
# 队头插入
user_deque.appendleft("sql")
# 对当前元素直接扩容，不做返回，参数必须是iterable的
user_deque.extend(user_deque)
print(user_deque)  # deque(['sql', 'Ivana', 'sql', 'Ivana'])
user_deque.extend(("haha"))  # 元祖中只有一个元素且不加逗号","时，例如("haha")，只作为一个值为"haha"的字符串，字符串可迭代
print(user_deque)  # deque(['sql', 'Ivana', 'sql', 'Ivana', 'h', 'a', 'h', 'a'])
user_deque.extend(("haha",))  # 元祖中只有一个元素但有逗号","时，例如("haha"，)，是元祖类型
print(user_deque)  # deque(['sql', 'Ivana', 'sql', 'Ivana', 'h', 'a', 'h', 'a', 'haha'])

# extendleft()
# index()
# insert()


# 浅拷贝，只做值的拷贝（元素值/引用值）
my_deque1 = deque(["Ivana", ["sql", "zyz"]])
# my_deque2 = my_deque1.copy()
# print(id(my_deque1[0]), id(my_deque2[0]))  # 相同，83091328 83091328
# print(id(my_deque1[1]), id(my_deque2[1]))  # 相同，82523912 82523912
# my_deque2[0] = "zyz"
# print(my_deque1, my_deque2)
# # output: deque(['Ivana', ['sql', 'zyz']]), deque(['zyz', ['sql', 'zyz']])
# my_deque2[1].append("liusiqian")
# print(my_deque1, my_deque2)
# # output: deque(['Ivana', ['sql', 'zyz', 'liusiqian']]) deque(['zyz', ['sql', 'zyz', 'liusiqian']])
# print(id(my_deque1), id(my_deque2))  # 不同，81751160 81751264
# print(id(my_deque1[0]), id(my_deque2[0]))  # 不同，83091328 82539496
# print(id(my_deque1[1]), id(my_deque2[1]))  # 相同，81807432 81807432
# my_deque2[1] = ["Ivana"]
# print(my_deque1, my_deque2)
# # deque(['Ivana', ['sql', 'zyz', 'liusiqian']]) deque(['zyz', ['Ivana']]
# print(id(my_deque1[1]), id(my_deque2[1]))  # 不同，81807432 81807112


# 深拷贝
my_deque3 = copy.deepcopy(my_deque1)
print(id(my_deque1), id(my_deque3))  # 不同
print(id(my_deque1[0]), id(my_deque3[0]))  # 相同
print(id(my_deque1[1]), id(my_deque3[1]))  # 不同
my_deque3[1].append("zhanyizhu")
print(my_deque1, my_deque3)
# output: deque(['Ivana', ['sql', 'zyz', 'liusiqian']]) deque(['Ivana', ['sql', 'zyz', 'liusiqian', 'zhanyizhu']])
print(id(my_deque1), id(my_deque3))  # 不同
print(id(my_deque1[0]), id(my_deque3[0]))  # 相同
print(id(my_deque1[1]), id(my_deque3[1]))  # 不同
my_deque3[0] = "zyz"
print(my_deque1, my_deque3)
# deque(['Ivana', ['sql', 'zyz', 'liusiqian']]) deque(['zyz', ['sql', 'zyz', 'liusiqian', 'zhanyizhu']])
print(id(my_deque1[0]), id(my_deque3[0]))  # 不同，83615672 82596896
