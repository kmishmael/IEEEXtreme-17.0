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

#usr/bin/env python 3

def iterator(a, b):
    num_list = [] # happy numbes
    for number in range(a, b+1):
        n = number
        sums = []
        l = 0
        while l < 7:
            l += 1
            s = sum(int(c)**2 for c in str(n))
            if s == 1:
                num_list.append(number)
                break
            if s in sums:
                break
            sums.append(s)
            n = s
    return len(num_list)


inputA = get_number()
inputB = get_number()

print(iterator(inputA, inputB)) # deal with input

