# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split('\n'))
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
#import numpy
#import scipy

def get_letter(len):
    space = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'

    len = len % 26
    return space[len]


num_inputs = get_word()
num_inputs = num_inputs.split(" ")
n = int(num_inputs[0])
m = int(num_inputs[1])

ryme_dict = {}
for i in range(0, n):
    ryme_dict[get_letter(i)] = [i.lower() for i in get_word().split(' ')]

ryme_lines = []
for i in range(0, m):
    ryme_lines.append([i.lower() for i in get_word().split(' ')])

output = ''

for line in ryme_lines:
    last_word = line[-1]
    #print('last word ', last_word)
    found = False
    for key, value in ryme_dict.items():
        #print('values ', value)
        if last_word in value:
            print(last_word, ' in ', value)
            output += key
            found = True
            break;
    if not found:
        output += 'X'
"""
for i in range(len(output)):
    if i - 1 < 0:
        if i + 1 > len(output) - 1:
            pass
        else:
            if i + 1
"""

def parse_string(input):
    if len(input) < 2:
        return 'X'
    for i in range(len(input)):
        if i - 1 < 0:
            pass
        else:
            if input[i - 1] == input[i]:
                continue
            else:
                if i + 1  < len(input) - 1:
                    if input[i+1] == input[1]:
                        continue
                    else:
                        input[i] = 'X'

    return input
print(output)
output = parse_string(output)

print(output)

print(f'rhymes: {ryme_dict} lines: {ryme_lines}')
