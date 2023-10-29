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
import numpy
import scipy

cases = get_number()

for case in range(1, len(cases) + 1):
    n = get_number()
    m = get_number()
    k = get_number() # bad consecutive coffees
    b = get_number() # bad level

    cube = []
    for _ in range(n):
        inner = []
        for _ in range(m):
            inner.append(get_number())
        cube.append(inner)

    def get_path(right):
        path = []
        if right:
            for i in range(len(cube)):
                path.append(cube[i][-1])
        else:
            for i in range(len(cube)):
                path.append(cube[i][0])
        return path


    right = get_path(True)
    left = get_path(False)

    count_r = 0
    right_b = True
    for i in range(len(right)):
        if right[i] < b:
            count_r += 1
        if count_r >= k:
            right_b = False
            break

    count_l = 0
    left_b = True
    for i in range(len(left)):
        if left[i] < b:
            count_l += 1
        if count_l >= k:
            left_b = False
            break;

    if right_b and left_b:
        print('Case ', case, max(sum(left), sum(right)))
    elif right_b:
        print('Case ', case, sum(right))
    else:
        print('Case ', case, sum(left))

    # print('Right: ', get_path(True))
    # print('Left: ', get_path(False))