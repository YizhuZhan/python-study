# -*- coding:utf-8 -*-
import functools


def cmp_by_id(d1, d2):
    if d1.get('id') < d2.get('id'):
        return -1
    elif d1.get('id') > d2.get('id'):
        return 1
    else:
        return 0


if __name__ == "__main__":
    my_dict = [
        {'id': '4', 'name': 'b'},
        {'id': '6', 'name': 'c'},
        {'id': '3', 'name': 'a'},
        {'id': '1', 'name': 'g'},
        {'id': '8', 'name': 'f'}
    ]
    # cmp在python3中被移除了，所以可以用functools包中的cmp_to_key来代替
    print(sorted(my_dict, key=functools.cmp_to_key(cmp_by_id)))