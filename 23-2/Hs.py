# class Person:
#     # data
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     # funct
#     def run(self):
#         print('runing ......' )
#     def __str__(self):
#         return f'{self.name} age {self.age}'
#
# p1 = Person('idan', 23, 29000)
# print(p1)


# class SuperHero:
#     def __init__(self, name):
#         self.name = name
#         print(f'new super hero {self.name} ')
#     def force_speed(self):
#         print('running ........')
#     def climb(self):
#         print('climbing ........')
#     def fly(self):
#         print('flying .......')
#     def __str__(self):
#         return  f'hello'
#
#
# s1 = SuperHero('superman')
# s2 = SuperHero('ironman')
# s3 = SuperHero('catwoman')
#
# s1.fly()
# s2.climb()
# s3.force_speed()
#
# print(s1)


class Actor:

    def __init__(self, first_name, last_name, salary, phrase):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.phrase = phrase

    def print_phrase(self):
        print(f'and {self.first_name} says : "{self.phrase}"')

    def tip_actor(self, tip):
        # self.salary += tip if tip < 1000 and tip % 2 == 1 else 0
        if tip < 1000 and tip % 2 == 1:
            self.salary = self.salary + tip


actor1 = Actor('joey', 'tribianni', 14000.0 ,'how you doin !! ')