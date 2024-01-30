t=int(input())
for _ in range(t):
    n = int(input())
    el=list(map(int,input().split()))
    for i in range(n-1):
        flag = 0
        for j in range(2):
            if el[j] < el[j+1]:
                tmp = el[j]
                el[j] = el[j+1]
                el[j+1] = tmp
                flag = 1
        if flag == 0:
            break
    print(el)

