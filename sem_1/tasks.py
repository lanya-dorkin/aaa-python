# task 1

# a = [0, 1, 2, 3, 4, 5]
# b = [3, 4, 5, 8]

# b_set = set(b)
# ans = [elem for elem in a if elem in b_set]

# print(ans)

# task 2

# a = [0, 2, 1, 0, 1, 2]

# # сохранение порядка
# ans = []
# prev = set()
# for elem in a:
#     if elem not in prev:
#         ans.append(elem)
#         prev.add(elem)
# print(ans)

# # без сохранения порядка
# ans = list(set(a))
# print(ans)

# task 3

# a = [0, 1, 2, 3, 4, 5]
# ans = [i for i in a if i % 2 == 0]
# print(ans)
# print(a[::2])

# task 4

# a = ['foo', 'bar', 'baz']
# b = {}
# for i in range(len(a)):
#     b[i] = a[i]
# print(b)

# task 5

# a = ['John', 'Allison']
# print(*[f'Hi, {name}!' for name in a], sep='\n')

# task 6

# a = ['foo', 'bar', 'baz', 'egg']
# b = ['bar', 'baz']

# b_set = set(b)
# ans = [i for i in a if i not in b_set]
# print('elements not in b: ', end='')
# print(*ans, sep=', ')

# print('not in b: ' + ', '.join(set(a) - set(b)))

# task 7

# a = list(range(9))
# b = [3, 4, 5]
# ans = list(sorted(set(a + b)))
# print(sorted(set(a + b)))

# task 8

# a = {0: 'foo', 1: 'bar', 2: 'baz'}
# print({k: a[k] for k in sorted(a, reverse=True)})

# task 9

import requests


url = 'https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'
response = requests.get(url).json()

for point in response['dataseries']:
    w = point['wind10m']
    print(f'направление: {w["direction"]}, скорость: {w["speed"]}')