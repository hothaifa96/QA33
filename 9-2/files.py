# r = open file for reading
# a = read and write with append mode add to exsit file >>
# w = override create file if not exsit and open in write mode
# x = create file
#
# t txt
# image audio binary

# log = open( 'log.txt' , 'a')
# text = input('enter you statement : ')
# log.write(text)
# log.write('\n \t')
# log.close()


#  name : {username}    address: {user address}    grade : {user grade}
# in append mode  ask the user to enter the info in 3 steps

# grades = open('/Users/hothaifa/Desktop/grades.txt','a') # create the file or open it if exist
#
# for i in range(22):
#     name = input('enter name ')
#     address = input('enter address ')
#     grade = input('enter grade ')
#     grades.write(f'name : {name} \t address : {address} \t grade : {grade} \n')
#
# grades.close()

# grades= open('/Users/hothaifa/Desktop/grades.txt','r')
# # grades.seek(500)
# # print(grades.read(100))
# # print(grades.tell())
# # # grades.seek(0)
# # # print(grades.read(120))
# #
#
# for line in grades:
#     print(line.find('hodi'))


# import os
# p = '/Users/hothaifa/Desktop/aa.png'
#
# if os.path.exists(p):
#     os.remove(p)

from PIL import Image

im = Image.open('/Users/hothaifa/Desktop/aa.png')

im.show()

# i = open('/Users/hothaifa/Desktop/aa.png','wb')
# print(i.read())