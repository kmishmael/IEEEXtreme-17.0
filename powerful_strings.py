# a simple parser for python. use get_number() and get_word() to read
from itertools import product

def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
# import numpy
# import scipy


n = get_number()
m = get_number()

s = []
space = "abcdefghijklmnopqrstuvwxyz"
for i in range(m):
    s.append(get_word())

print(n, m, s)

def count_strings(length, substrings):
    combinations = list(product(*substrings))
    count = 0

    #print(len(list(product(space, repeat=length))))
    for chars in product(space, repeat=length):
        current_string = ''.join(chars)
        print(type(combinations))
        print(type(current_string))
        for i in combinations[:1]:
            print('tuple: ', 'b' in i[1])
            print(type(i))
        for i in current_string[:1]:
            print('string: ', i)
            print(type(i))
        #if all(for sub in substring for sub in current_string for sub in substring for substring in combinations):
         #   print(type(combinations))
          #  count += 1
        if all([True]):
            #print(type(combinations))
            count += 1

    return count
print('s ', s)
count_strings(n, s)