# -*- coding:utf-8 -*-


class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        print (kw)
        for key in kw:
            setattr(self, key, kw[key])


p = Person('Bob', 'Male', age=18, course='Python')


print(p.age)
print(p.course)
print(getattr(p, 'gender', 'Female'))
print(getattr(p, 'grade', 1))
setattr(p, 'grade', 2)
print(getattr(p, 'grade', 1))


print(type(p))
dir_list = dir(p)
print(dir_list)
print(list(filter(lambda s: False if s.startswith('__') and s.endswith('__') else True, dir_list)))


