import types


def get_grade(self):
    if self.score >= 90:
        return "A"
    elif self.score < 60:
        return "C"
    else:
        return "B"


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person("Ivana", 95)
p1.get_grade = types.MethodType(get_grade, p1)
print(p1.get_grade())
