# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘PyTest’

# !/usr/bin/env python
'''
类的继承和重写
'''
class Person(object):
    '''
    返回具有给定名称的person对象
    '''
    def __init__(self, name):
        self.name = name

    def get_details(self):
        '''
        返回包含人名的字符串
        '''
        return self.name

class Student(Person):
    '''
    返回Student对象，采用name，branch，year3个参数
    '''
    def __init__(self,name, branch, year ):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        '''
        返回包含学习信息的字符串
        '''
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

class Teacher(Person):
    '''
    返回Teacher对象，采用字符串列表作为参数
    '''
    def __init__(self, name, papers):
        Person.__init__(self, name,)
        self.papers = papers

    def get_details(self):
        '''
        返回包含老师信息的字符串
        :return:
        '''
        return "{} teaches {}.".format(self.name, self.papers)

person1 = Person('Sachin')
student1 = Student('Kushal', 'SCE', 2018)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())