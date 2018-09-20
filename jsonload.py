# -*- coding:utf-8 -*-
import json


class Students(object):
    def __init__(self, namelist):
        self.namelist = namelist

    def read(self):  # 有read方法的类是File-like Object，可以由json.load()解析
        return self.namelist


s1 = Students('["Tim", "Bob", "Alice"]')
print(json.load(s1))
