# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid value')
        self.__score = score

    # 只设置getter而不设置setter，只读属性
    @property
    def grade(self):
        if self.score >= 80:
            return 'A'
        elif self.score < 60:
            return 'C'
        else:
            return 'B'


s1 = Student("Ivana", 95)
print(s1.score)
s1.score = 80
print(s1.score)

try:
    s1.score = 101
except ValueError as e:
    print(e.args)
finally:
    print(s1.score)

try:
    s1.grade = 'D'
except AttributeError as e:
    print(e.args)
finally:
    print(s1.grade)


class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):

    __slots__ = ('age',)

    def __init__(self, name, gender, age):
        # python3中用super().__init__(参数)，python2中用super(子类名，self).__init__(参数)
        super().__init__(name, gender)
        self.age = age


p = Person('Bob', 'male')
# 由于slots的限制，不能对Person对象添加score属性
try:
    p.score = 59
except AttributeError as e:
    print(e.args)


s = Teacher('Bob', 'male', 59)
s.name = 'Tim'
s.age = 30
print(s.age)
try:
    s.score = 100
except AttributeError as e:
    print(e.args)




