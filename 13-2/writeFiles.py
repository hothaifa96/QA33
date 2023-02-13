
file = open('/Users/hothaifa/Desktop/loz/file1.txt','r+')

file.write('yarin is the best')
file.seek(0)
print(file.read())

file.close()