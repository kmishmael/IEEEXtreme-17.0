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
s_dict = {}

ryme_list = []
for i in range(0, n):
    ryme_list.append([i.lower() for i in get_word().split(' ')])

ryme_lines = []
for i in range(0, m):
    ryme_lines.append([i.lower() for i in get_word().split(' ')][-1])


def get_letter(len):
    space = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'

    len = len % 26
    return space[len]

def get_next_letter(output, last_word):
    found = False
    for k, v in s_dict.items():
        if last_word in v:
            found = True
            letter = ord(k)
    if found == False:
        c = [x for x in output if x != 88]
        f = max(c)
        letter = 65 + (f + 1) % 26
        for l in ryme_list:
            if last_word in l:
                s_dict[chr(letter)] = l
    return letter

output = []
for index, last_word in enumerate(ryme_lines):
    for grp in ryme_list:
        if last_word in grp:
            # lets look around
            if index - 1 < 0:
                if(index + 1 < len(ryme_lines) - 1):
                    if ryme_lines[index + 1] in grp:
                        output.append(65) # sure
                        s_dict['A'] = grp
                    else:
                        output.append(88) # sure
                else:
                    output.append(88) # sure
            elif index + 1 > len(ryme_lines) - 1:
                if(index - 1 < len(ryme_lines) - 1):
                    if ryme_lines[index - 1] in grp:
                        output.append(output[-1])
                    else:
                        output.append(88)
                else:
                    output.append(88)
            else:
                if ryme_lines[index - 1] in grp:
                    output.append(output[-1])
                elif ryme_lines[index + 1] in grp:
                    if ryme_lines[index - 1] in grp:
                        output.append(output[-1])
                    else:
                        output.append(get_next_letter(output, last_word))
                else:
                    output.append(88)

print(output)
