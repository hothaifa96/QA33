# download requests using pip  : pip install requests
import requests


# # making GET request
# res = requests.get('https://jsonplaceholder.typicode.com/users')
#
# # check the status
# print(res.status_code)
# if 200 <= res.status_code < 400:
#     print('success')
# else:
#     print('ERROR')
#
# users = res.json() # dict
# print(users[0]['name'])
#
# for user in users:
#     print(user['name'] , user['email'])


# send GET http request to
# https://jsonplaceholder.typicode.com/photos
# 0- print success if the request valid and return 2XX
# 1- print the title of each photo
# 2- print the amount of photos in this site
# 3- print all the urls contains '66'

def send_http_request(url):
    res = requests.get(url)
    return res


def check_status_code(code):
    if 200 <= code < 400:
        print(f'success status code -> {code}')
        return True
    else:
        print('ERROR')
        return False


# for photo in photos:
#     print(photo['title'])
#
# print(f'\nwe have -> {len(photos)} photos \n')
#
# counter = 0
# for photo in photos:
#     if '66' in photo['url']:
#         counter += 1
#         print(photo['url'])
# print(counter)
