# # x = 10
# # y = 16
# #
# # # x = 1 + x
# # x +=1
# #
# # # str -> text
# # # number -> 4 , 15.1 -22
# # # bool -> True, False
# # # complex numbers ->  a+bi -> i sqrt(-1)
# #
# # print(x)
#
# # declare a variable called name with you name
# # in lowercase and lastname with upper case
#
# # x = '123456789'
# # # print( name.capitalize() ) #convert the first char to upper case
# # # print(name.upper()) #convert all the chars to upper
# # # print(name.lower()) # convert all the chars to lower case
# # # print(name.isspace())
# # # print( len(name) ) length of string
# # # index of string is the cell number starting from 0
# # #  x[(index)] index is a number
# # #  x[(index):(index)] return a range of chars between the two indexes
# #
# # print(x[2]) # 3
# # print(x[-1]) #9
# # print(x[3:7]) # 4567
# # # 789 2 methods
# # print(x[6:])
# # print(x[-3:])
#
#
# first_name = 'gila'
# last_name = 'Biru'
#
# # print(name.find('a')) # return the first appear of char
# # print(name.replace(' ', '*')) # replace old char with new char
# # print(name.count(' gal')) # retrun the count of a string in another string
# # print(name.endswith('rU'))
# # print(name.startswith('gi'))
# # print(name.isnumeric())
# # print(name.isalpha())
# # print(name.isupper())
#
# # print(first_name + ' ' + last_name)
# print(f'the fullname is {first_name}  {last_name}')
# print(first_name, last_name)

# declare first_name variable with your name as string
# declare last_name variable with you last name
# declare full_name variable witch is the concat
# of your firstname and lastname
# print the full name and if its start with you first
# name print True if it's not print false
# starswith  + or f'{} {}'   full_name=

# first_name = 'chen'
# last_name = 'davidzon'
# full_name = f'{first_name} {last_name}'
# print(full_name)
# print(full_name.startswith(first_name))

# first_name = input('please enter your first name: ')
# last_name = input('please enter your last name: ')
# full_name = f'{first_name} {last_name}'
# print( f'hello {full_name}')
# print(full_name.startswith(first_name))

# write a code to receive a name for a user
# and print the last 2 chars of his name

name = input('enter your name :')
print(name[-2:])
