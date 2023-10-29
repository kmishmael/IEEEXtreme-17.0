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


n = get_number()
m = get_number()

s = []
modulus = 998244353
space = "abcdefghijklmnopqrstuvwxyz"
for i in range(m):
    s.append(get_word())

print(n, m, s)

def count_substrings(s, subs):
    total_count = 0
    for sub in subs:
        index = -1
        while True:
            index = s.find(sub, index + 1)
            if index == -1:
                break
            total_count += 1
    return total_count

def calculate_power(base, exponent):
    if modulus == 1:
        return 0
    res = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            res = (res * base) % modulus
        exponent //= 2  # divide by 2
        base = (base * base) % modulus
    return res

def main():
    n = get_number()
    m = get_number()
    substrings = []

    for i in range(m):
        substrings.append(get_word())

    total_power = 0
    space = 'abcdefghijklmnopqrstuvwxyz'

    stack = [('', n)]

    while stack:
        current_string, length = stack.pop()

        if length == 0:
            total_count = count_substrings(current_string, substrings)
            power = calculate_power(2, total_count)
            total_power = (total_power + power) % modulus
        else:
            for i in range(len(space)):
                stack.append((current_string + space[i], length - 1))

    print(total_power)
    return total_power

main()