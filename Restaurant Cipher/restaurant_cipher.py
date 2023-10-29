from collections import Counter
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

testCases = get_number()

codes = []

for test in range(testCases):
    codes.append(get_word())
    
# print('Sentences ->', codes)
    
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
symbols2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for k in range(len(codes)):
    sentence = codes[k]
    newList = []
    common = 1
    for character in range(len(sentence)):
            char = sentence[character]
            if char!=' ':
                newList.append(char)
            else:
                continue
    count = Counter(newList)
    newSet = set(newList)
    freq = count.most_common(1)[0][0]
    if freq in symbols:
        if freq == 'a':
            freq = 'A'
        elif freq == 'b':
            freq = 'B'
        elif freq == 'c':
            freq = 'C'
        elif freq == 'd':
            freq = 'D'
        elif freq == 'e':
            freq = 'E'
        elif freq == 'f':
            freq = 'F'
        elif freq == 'g':
            freq = 'G'
    else:
        freq = 'G'
    print(freq)
    # print(newSet)