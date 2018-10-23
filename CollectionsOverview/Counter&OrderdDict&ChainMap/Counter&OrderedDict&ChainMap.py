# -*-coding=utf-8 -*-
__author__ = 'Ivana'
from collections import Counter, OrderedDict, ChainMap


# Counter(传入iterable参数)，返回一个字典{key: num}
str_counter = Counter("hahaaa")
print(str_counter)  # Counter({'a': 4, 'h': 2})
users=["Ivana1", "Ivana2", "Ivana3", "Ivana1", "Ivana2", "Ivana2"]
user_counter = Counter(users)
print(user_counter)  # Counter({'Ivana2': 3, 'Ivana1': 2, 'Ivana3': 1})


# update(iterable)可传入更多字符串进行合并统计
user_counter.update(["zyz", "sql", "zyz", "zyz", "zyz"])
print(user_counter)  # Counter({'zyz': 4, 'Ivana2': 3, 'Ivana1': 2, 'Ivana3': 1, 'sql': 1})


# most_common()可统计出现次数最多的前n个元素（top n问题）
# 源码中是直接调用了_heapq.nlargest(...)，利用堆来专门解决top n问题，性能好很多
n = 1
user_top_n = user_counter.most_common(n)
print(user_top_n)  # [('zyz', 4)]
m = 2
user_top_m = user_counter.most_common(m)
print(user_top_m)  # [('zyz', 4), ('Ivana2', 3)]


# OrderedDict:可排序字典, 在python2以下无序，在python3开始，以添加先后为顺序
# nameedtuple中的__asdict()方法返回类型就是OrderedDict
my_ordereddict = OrderedDict({'language': "Ch/En", 'hobby': "swimming"})
my_ordereddict['height'] = 167
my_ordereddict['name'] = 'Ivana'
# 把指定键的item移到最后
my_ordereddict.move_to_end('hobby')
# 弹出尾部(键, 值)
print(my_ordereddict.popitem())  # ('hobby', 'swimming')
# 指定键，弹出值
print(my_ordereddict.pop('language'))  # Ch/En
print(my_ordereddict)  # OrderedDict([('height', 167), ('name', 'Ivana')])


user_dict1 = {"name": "Ivana", "age": 27}
user_dict2 = {"name": "sql", "age": 28}
# ChainMap将两个dict合起来，并保持原样，只是增加了一个迭代器，而没有做去重
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict)  # ChainMap({'name': 'Ivana', 'age': 27}, {'name': 'sql', 'age': 28})
# 但是遍历时，会模拟一个dict进行操作，会去重，使得访问多个dict就像访问一个dict一样方便
for k, v in new_dict.items():
    print((k, v))
    # ('age', 27) ('name', 'Ivana')


# new_dict.maps返回一个数组，maps为指向该数组引用
print(new_dict.maps)
# output: [{'name': 'Ivana', 'age': 27}, {'name': 'sql', 'age': 28}]

