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

n = get_number()
h0 = get_number()
a = get_number()
c = get_number()
q = get_number()
heights = []
heights.append(h0)

for people in range(n):
    newH = (a*h0+c)%q
    heights.append(newH)
    h0 = newH
heights.pop()
heights.reverse()
# print(heights)
length = len(heights) - 1
# print(length)
# indexM = length
visible = 0
for h in range(len(heights)):
    barrier = heights[h]
    last_visible = 0
    for k in range(h+1, len(heights)):
        if k == h+1:
            visible = visible + 1
            last_visible = heights[k]
        else:
            if heights[k] > last_visible:
                visible = visible + 1
                last_visible = heights[k]
            else:
                continue

print(visible)

# visible = []
# notice = 0
# ahead3 = 1
# diff = []

# for h in range(len(heights)):
#     index3 = indexM - 1
#     s_diff = []
#     while index3 >=0:
#         diff2 = heights[indexM] - heights[index3]
#         s_diff.append(diff2)
#         index3 = index3 - 1
#     indexM = indexM - 1
#     diff.append(s_diff)
# diff.pop()

# for h in range(len(heights)):
#     # ahead = 1
#     # ahead2 = 1
#     # person = heights[length]
#     if length == 0:
#         pass
#     else:
#         for he in range(len(diff[h])):
#             ahead = 
#             print(he)

       # while True:
            # visible.append(heights[length-ahead])
            # if person<heights[length-ahead]:
            #     ahead = ahead+1
            # else:
            #     break

          #  notice = notice + 1
    #length = length-1

#print('Differences ->', diff)
# print(visible, notice)
# length = len(heights) - 1
# diffnum = length
# lengthd = len(diff) - 1
# for d in diff:
#     while diffnum >0:
#         present = abs(diff[lengthd])
#         notice = notice+1
#         if present < abs(diff[lengthd+1]):
#             continue
#     diffnum = diffnum -1
# print(diff, lengthd, notice)