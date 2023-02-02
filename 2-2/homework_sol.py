# x = int(input('enter something'))   # str
# x = float(input('enter something'))   # str
#
# print(x)

#2

# food = 'pizza and salad'
#
# if 'koskos' in food :     # in ->  contains
#     print(food)

# if condition :
#     true block
# elif :
#     false block
#
# else
# elif

#4
# x = int(input('please enter a number : '))
# y = int(input('please enter a number : '))
# if x > y:
#     print(f'{x} greater than {y}')
# elif y > x:
#     print(f'{y} greater than {x}')
# else:
#     print(f'x and y equals')

#  print(max(x, y))

#5

# x = int(input('enter a number: '))
# y = int(input('enter a number: '))
# z = int(input('enter a number: '))
#
# # if x > y and x > z :
# #     print(x)
# # elif y > z :
# #     print(y)
# # else:
# #     print(z)
#
# print(max(x,y,z))

#6

# number1= int(input('enter the first number '))
# operator= input('enter the operator ')
# number2= int(input('enter the second number '))
# ans = int(input('answer '))
#
# if operator == '+' :
#     print( ans == number2 + number1 )
# elif operator == '-' :
#     print( ans == number2 - number1 )
# elif operator == '*' :
#     print( ans == number2 * number1 )
# elif operator == '%' :
#     print( ans == number2 % number1 )


# row = input('enter => ')
# # 4 + 15 = 1
#
# end = row.find('+') - 1
# end2 = row.find('=') -1
# x = int(row[:end])
# y= int(row[end+3:end2])
# ans =int (row[end2+3:])
#
# if x+y ==ans:
#     print(True)
# else:
#     print(False)