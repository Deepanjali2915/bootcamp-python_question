n=int(input())
i=1
count=0
while i<n:
    if n%i==0:
        count=count+i
        # print(count)
    i+=1
# print(count)    
if n==count:
    print("YES")
else:
    print("NO")      