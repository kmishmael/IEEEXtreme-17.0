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

ryme_list = []
for i in range(0, n):
    ryme_list.append([i.lower() for i in get_word().split(' ')])


ryme_lines = []
for i in range(0, m):
    ryme_lines.append([i.lower() for i in get_word().split(' ')][-1])

print('dict =>', ryme_list)
print('lines => ', ryme_lines)
output = ''

ryme_dict = {}
idx = 0
already_tracked = []
for index, last_word in enumerate(ryme_lines):

    for r in ryme_list:
        if last_word in r and last_word not in already_tracked:
            already_tracked.extend(r)
            ryme_dict[get_letter(idx)] = r
            idx += 1

    found = False
    for key, value in ryme_dict.items():
        #print('values ', value)
        if last_word in value:
           # print(last_word, ' in ', value)
            output += key
            found = True
            break
    if not found:
        output += 'X'

print('ryme_dict => ', ryme_dict)
print('already tracked => ', already_tracked)

def parse_string(input):
    input = [char for char in input]
    # print('input => ', input)
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
                    if input[i+1] == input[i]:
                        continue
                    else:
                        input[i] = 'X'

    return ''.join(input)
output = parse_string(output)

print(output)

#print(f'rhymes: {ryme_dict} lines: {ryme_lines}')

"""
2 6
hash dash crash slash
underscore four

Waka waka bang splat tick tick hash
Caret quote back tick dollar dollar dash
Bang splat equal at dollar underscore
Percent splat waka waka tilde number four
Ampersand bracket bracket dot dot slash
Vertical bar curly bracket comma comma CRASH
"""