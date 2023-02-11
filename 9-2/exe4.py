# 2
# list = [100, 8, 7, 1, 2, 5, 1, 61, 11, 6]
# for i in range(len(list) // 2):
#     print(list[i])
#
# print('-------------------')
# list2 = list[:len(list) // 2]

# 3
# words= ['qa and automation','java','fun','python','hello']
# #
# # for word in words :
# #     print(word.upper())
#
# #4
#
# for word in words:
#     if len(word) < 4:
#         break
#     print(word.upper())

# 4

# fullname = 'matan slomon'
# print(fullname[-5:])
# print(fullname[: len(fullname) // 3])
# print('count:', fullname.count('a'))
# # count = 0
# # for l in fullname:
# #     if l =='a':
# #         count += 1
# # print('for :',count)
# # if fullname.count('b') == 0 :
# #     print(False)
# # else:
# #     print(True)
# print(fullname.count('b') != 0)
# # is_b = False
# # for lt in fullname:
# #     if lt == 'b':
# #         is_b = True
# # print( is_b )
#
# # if fullname == 'shahar hasson':
# #     print('shushhhiiii')
# # else:
# #     print('go have a drink')
# #
# # print('shushhhiiii' if fullname == 'shahar hasson' else 'go have a drink')
# # # true blick   if condi   else    false block
# names = fullname.split()
# print(names)
# names.reverse()
# print(names)
# names[0] = names[0].upper()
# print(names)
# # names[1] = names[1].replace(names[1][(len(names[1])//2)], '')
# names[1] = names[1].replace('t', '')
# print(names)
#
# fullname2 = names[0] +' '+ names[1]
# print(fullname)
# print(fullname2)
# print('hello', end='@gmail.com \n')
#
# # [1,4,9,16,25,36]
# list = [i ** 2 for i in range(1, 7)]
# even = [x for x in range(100) if x % 2 == 0]
# # declare a list using for with all the numbers between 1 and 6 powered by 2
# # for i in range(1, 7):
# #     list.append(i**2)
# # print(list)
# print(list)
# print(even)
