a=[11,113,21,3,7]
b=int(input())
i=0
count=0
while i<len(a):
    if a[i]==b:
        count+=1
    i+=1
if count>=1:
    print("YES")
else:
    print("NO")                