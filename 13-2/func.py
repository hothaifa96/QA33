import random
def greet():
    for i in range(5):
        print('hello')


def greet_with_name(name):
    print('hello '+name)


def greet_with_name_and_age(name, age):
    print(f'my name is {name} and im {age} years old')

# greet()
# print('joey doesnt share food')
# greet_with_name('yaniv')
# k1= input('enter your name ')
# greet_with_name(k1)
# greet_with_name_and_age('matan',90)


def my_max(x, y):
    return x if x > y else y


def the_other_half(text):
    half = len(text)//2
    return text[half:]


def my_random():
    return 5


mx = my_max(66, 77)
h = the_other_half('banana')
print(h)
number = my_random()
print(number)
