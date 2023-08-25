import sys
a = input()
i = 0
dict = {}
for n in a:
    dict[i] = n
    i +=1

b = i - 1
w = 0
for c in range(b):
    d = dict[w]
    p = dict[b]
    f = w + 1
    if f == b:
        break
    if d != p:
        print('false')
        sys.exit()
    w +=1
    b -=1

print('true')