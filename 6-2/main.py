# name1='lior'
# name1= 5
#
# names = ['lior','yara','noy','bar', 'gal']
# # print(names)
# # print( names[2] )
# # names.append('omniya')
# # print(names)
# # names.pop(3) # remove by index or remove the last item
# # print(names)
# # names.remove('gal') # delete by value
# names[3] = 'yarin'
# print(names)

# loops
# for x in range(3):
#     w = input('enter name')
#     print(w)
# print('thank you')

# for i in range(5,-6,-1):
#     print('hello ',i)

# range(n) =>  0,1,2,3,.....n-1    n -> positive and int
# range(l,h) => l,l+1,l+2 ..... h-2, h-1  -> l,h positive and int and h > l
# range(3,5) => 3,4
# range(10,100) => 10,11,12,13,.....98,99
# range(b1,b2,j) => b1 , b1 +  j , b1 + (j*2) ,..... b2 - j
# range(1,100,4) => 1 , 5, 9, 13,17 .....
# range (5,-6 ,-1) -> 5,4,3,2,1,0,-1,-2,-3,-4,-5

# for x in range(50,101,2):
#     print(x)
#
# for x in range(100):
#     if x >= 50 and x %2 ==0:
#         print(x)


# name = 'yarin shmaryahoo'
# # dessert = 'knafeh'
# # # count = 0
# # # for i in dessert:
# # #     if i == 'n':
# # #         count += 1
# # # print(count)
# #
# rev_name = ''
# #
# for i in range(len(name)-1 , -1 , -1): #'=> ( 8,7,6,5,4,3,2,1,0 )'
#     rev_name += name[i]
# print(rev_name)


# name = 'einav cohen'
#
# for lt in range(len(name)-1, 0,-1):
#     print( name[lt] ,end='' )


# foods = ['flafel', 'kfeltafish', 'kreplah', 'shawarma', 'pizza', 'cookie', 'sabikh']
#
# for i in range(len(foods)):
#     if len(foods[i]) > 6:
#         print(foods[i])
#         foods[i]=''
# print(foods)


# קלטו מהמשתמש מספר שלם והדפיסו את כל המספרים מ 0 עד אותו מספר
# n = int(input('enter a number : '))
# for i in range(n+1):
#     print(i)

# קלטו מהמשתש את שמו והדפיסו את השם שלו 4 פעמים
# for i in range(4):
#     name = input('enter your name : ')
#     print(name)

# print only the colors have the letter r in it ['red','blue', 'green'
# , 'yellow' ,'pink']

# colors = ['red','blue', 'green', 'yellow' ,'pink']
# for color in colors:
#     if 'r' in color:
#         print(color)


# print whether the number positive or a negative in this list
# [1,2,3,-6,-8,55,-9972]

# numbers = [1, 2, 3, -6, -8, 55, -9972]
#
# for number in numbers:
#     if number >= 0 :
#         print('positive' , number)
#     else:
#         print('negative' , number)
