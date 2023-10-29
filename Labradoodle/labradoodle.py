(n, m) = list(map(int, input().split(" ")))
dictionary = []
for i in range(n):
    dictionary.append(input())

words = []
for i in range(m):
    words.append(input())


def findCommons(word, q):
    left = ""
    right = ""
    s = ""
    for i in word:
        s += i
        if s in q:
            if len(s) >= 3:
                left = s
        else:
            break

    for i in range(1, len(word)):
        if word[i:] in q:
            if len(word[i:]) >= 3:
                right = word[i:]
        else:
            break

    return [left, right]


def findMatch(word):
    left = []
    right = []
    for q in dictionary:
        for common_part in findCommons(word, q):
            if len(common_part) >= 3:
                if (word.startswith(common_part)):
                    left.append(q)
                elif (word.endswith(common_part)):
                    right.append(q)

    if len(left) == 1 and len(right) == 1:
        print(left[0], right[0])
        return
    elif len(left) > 1 or len(right) > 1:
        print("ambiguous")
        return
    else:
        print("none")
        return


for word in words:
    findMatch(word)