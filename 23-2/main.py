# OOP
# inheritance

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('sleeping . . . . . .')


class Lion(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def sleep(self):
        print('heheeeeww ...')

    def eat(self):
        print('eating ......')

class soso(Lion):
    pass

l1 = Lion('mofasa', 13, 44)

list1 = [l1, Animal('name', 11)]

for a in list1:
    a.sleep()
#
#
# class Employee():
#     def __init__(self, name, age, salary):
#         self.age = age
#         self.name = name
#         self.__salary = salary
#
#     def getSalary(self):
#         return '$$$$$'
#
#
# emp = Employee('hodi', 20, 2000)
# print(emp.getSalary())
