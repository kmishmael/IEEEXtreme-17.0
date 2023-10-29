# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        # end = []
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)
            # else:
            #     return 123
            #if number == data[-1]:
                # end.append(number)
                # end.append(15)
                # return end

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

def testShift(value):
    try:
        return int(value)
    except ValueError:
        return  101
    

# numpy and scipy are available for use

testCases = get_number()

sententeces = [] # list of strings
shift_list = []
flags = []

for i in range(testCases):
    shift_list.append(get_number())
    sententeces.append(get_word())

# shiftCount = 0
# shiftsList = []

for sentence in sententeces:
    s = sentence.split(' ')
    if 'the' in s:
        flags.append(True)
    else:
        flags.append(False)
    # print('S ->', s)
    # print('Flags ->', flags)


for k in range(len(sententeces)):
    sentence = sententeces[k]
    shift = int(shift_list[k])
    Letter = ''
    if flags[k]:
        
        for character in range(len(sentence)):
            char = sentence[character]

            char = ord(char)

            if char > 96 and char < 123: 
                char2 = char - shift
                if char2 < 97:
                    char2 = char2 + 26
                char = chr(char2)
                Letter = Letter + char
            else:
                char = chr(char)
                Letter = Letter + char

    else:
        for character in range(len(sentence)):
            char = sentence[character]

            char = ord(char)

            if char > 96 and char < 123: 
                char2 = char + shift
                if char2 > 122:
                    char2 = char2%122+96
                char = chr(char2)
                Letter = Letter + char
            else:
                char = chr(char)
                Letter = Letter + char
    print(Letter)
