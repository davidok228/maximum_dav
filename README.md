a = input()
i = 0
dict = {}
for n in a:
    dict[i] = n
    i +=1

for c in range(i):
    w = 0
    if w == i:
        break()
    if dict[w] != dict[i]:
        print('false')
        break()
    w +=1
    i -=1

print('true')

