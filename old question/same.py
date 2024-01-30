n=int(input("aa"))
for _ in range(n):
    t=list(map(int,input().split()))
    count=0
    i=0
    while i<=(len(t)-1):
        if t[0]==t[i]:
            count+=1
        i+=1
    if count==n:            
        print("Yes")
    else:
        print("NO")