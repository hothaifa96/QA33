# str
# int
# float
# bool
# list
# set
# tuple

# class ->  blueprint  Person - Car - Animal Dog
# object -> instance of class -> noy - gila - bar
#
# Dog -> jojo gibur

# class Dog:
#     def bark(self):
#         print('raph raph ..... '+str(self))
#
#     def walk(cls):
#         print('waling .... . .. .. .. ')
#
#     def eat(self, fav_food):
#         print(f'eating my fav food {fav_food}')
#
#     def calc_age(self, year):
#         return 2023 - year
# x = 5
# y = int('5')
#
# jojo = Dog()
# sofie = Dog()
# print(jojo)
#
# jojo.bark()
# sofie.bark()
# sofie.eat('bunzo')
# age = sofie.calc_age(2021)
# print(age)
# # Dog.walk(Dog)
#



# class Circle:
#
#     def draw(self):
#         print('drawing . . . .  ')
#
#     def calc_area(self, radius):
#         return 3.14 * radius ** 2
#
#
# c1 = Circle()
# c1.draw()
# print(c1.calc_area(5))
# print(isinstance(c1, Circle)) # checks if instance of the class
# print(type(c1)) # returns the class of an instance
# print(c1)



# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def draw(self):
#         print(f'drawing .... a -> {self.a}   b -> {self.b}')
#
#
# rec1 = Rectangle(10,5)
# rec2 = Rectangle(16,5)
# print(rec1.a)
# print(rec2.a)
# rec1.draw()
# rec2.draw()


# class Pizza:
#     def __init__(self, size, topping='cheese'):
#         self.size = size
#         self.topping = topping
#
#     def bake(self):
#         print(f'baking the {self.size} in the oven')
#
#
# p1 = Pizza('XXL','corn onions')
# p2 = Pizza('L','olives')
# p3 = Pizza('S')
#
# p2.bake()
#
# print(f'the size of the pizza is : {p1.size} and the topping: {p1.topping}')

class Employee:

    def __init__(self, name, birth_year, salary, car):
        self.name = name
        self.birth_year = birth_year
        self.salary = salary
        self.car = car


    def whats_my_name(self):
        print(f'name: {self.name}')

    def my_age(self):
        return 2023-self.birth_year

    def raise_my_salary(self):
        self.salary += 500

    def __eq__(self, other):
       return self.salary == other.salary

    def __gt__(self, other):
        ''' self > emp1.salary -> 14000 '''
        return self.birth_year < other.birth_year

    def __str__(self):
        return f'employee name :{self.name} , salary: {self.salary} , car:{self.car} , age: {self.my_age()}'


emp1 = Employee('inbar', 1999, 25000.0, 'audi rs7')
emp2 = Employee('miriam', 2000, 25000.0, 'bmw m4')

# emp1.whats_my_name()
# print(emp1.my_age())
# print(emp1.salary)  # emp1.salary -> 14000
# emp1.raise_my_salary()
# print(emp1.salary)  # emp1.salary -> 14500
print(emp1 == emp2)
print(emp2 < emp1)
