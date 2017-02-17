'''
Created on 2017年2月8日

@author: Administrator
'''


class Person(object):
    
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')
            
    def __eq__(self, other):
        if isinstance(other, Person):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('the type must be Person')

a1 = Person('Albert', 25)
b2 = Person('Lily', 27)
c3 = Person('Wayne', 27)

print(a1.age)
print(b2.name)
print(b2 == c3)
