# define a function to print yaouza 4 times
# def function1():
#     for i in range(4):
#         print('yaouza')
#
# function1()
# define a function to print a word of the user choice using input
#
# def function2():
#     word = input('enter a word :')
#     print(word)
#
# function2()


# a golden name is a name with 6 letters and includes i in it
# define a function to print if the given name is golden or not

# def function3(name):
#     if 'i' in name and len(name)==6:
#         print('golden name you have there ')
#     else:
#         print('naaah you should change it')
#
#
# function3('dandin')  # -> 'ia' 'aaa'  "aiaaaa" 'hothaf'

# define a function to receive a text as argument and add it to a
# text file named aa.txt and call it log

def log(text):
    try:
        file = open('aa.txt','a') # connecting to the file
        file.write('\n') # new line
        file.write(text) # add the text to the file
    except:
        print('error ')


log('hello')












