n=int(input())
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count<=2:
    print("Yes")
else:
    print("NO")            