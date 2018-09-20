# -*- coding:utf-8 -*-


class Person(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def how_many(cls):
        return cls.count

p1 = Person("Ivana")

print(p1.how_many())
print(Person.how_many())
