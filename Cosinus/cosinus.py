import math

# a simple parser for python. use get_number() and get_word() to read
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

t = get_number()

angles = []

for i in range(t):
    angles.append(get_number())

def smallest_integer_for_cos(angle):
    min_cos = float('inf')
    min_n = 1

    for n in range(1, 1000000):
        cos_value = abs(math.cos(math.radians(n * angle)))
        if cos_value < min_cos:
            min_cos = cos_value
            min_n = n
        print(min_cos)
        if min_cos == 0:
            return n

    return min_n

for a in angles:
    print(smallest_integer_for_cos(a))