
# print all the numbers from 1- 11
for i in range(1,12):
    print(i)
# declare a str name with your full name
# convert the name to a list and print the second item
# of this list
name ='hothaifa zoubi'
name_list = name.split()
print(name_list[1])
# Write a program to accept a number from a user and
# calculate the sum of all numbers from 1
# to a given number
number = int(input('enter a number : '))
sum = 0
for i in range(1,number+1):
    sum += i
print(sum)

# str.split()    range(start,end,jump)   [0,1,2,3]
# for i in range():
# sum+= i