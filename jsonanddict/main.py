# l1 = [1, 2, 3, 4, 55, 6, 7, 9, 9, 9, 9, 9]
# t = (1, 2, 3, 4, 66, 88)
# s = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9}
# s.add('hodi')
# print(s)
import json
d1 = {
    'name': 'yarden',
    'age': 23.86,
    'salary': 24000,
    'car': 'a1 s-line'
}
#
# print(d1)
# d1['married'] = False
# print(d1)
#
# for keys in d1.keys():
#     print(f'{keys} -> {d1[keys]}')
#
# print(d1.get('name111'))

print(d1)
json1 = json.dumps(d1)
print(json1)
print(json.loads(json1))