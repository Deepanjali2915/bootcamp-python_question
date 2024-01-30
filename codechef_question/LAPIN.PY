t=int(input())
for i in range(t):
    s=input()
    a=list(s[:len(s)//2])
    b=s[::-1]
    c=list(b[:len(b)//2])
    d=sorted(a)
    e=sorted(c)
    if d==e:
        print("YES")
    else:
        print("NO")
    
    

