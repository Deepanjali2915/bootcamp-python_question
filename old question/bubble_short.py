el = [-15,-33,-72,-72,-1]
n = len(el)
for i in range(n-1):
    flag = 0
    for j in range(n-1):
        if el[j] > el[j+1]:
            tmp = el[j]
            el[j] = el[j+1]
            el[j+1] = tmp
            flag = 1

    if flag == 0:
        break
print(el)

