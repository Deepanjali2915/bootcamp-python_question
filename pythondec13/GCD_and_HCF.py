m,n=map(int,input().split())
if m>n:
    max=m 
    min=n
else:
    max=n
    min=m
number=max
if number%min!=0:
    number+=max
    print(number)            
else:
    print(m*n)