a="abcdefgh"
b=input()
i=0
count=0
while i<len(a):
    # print(a[i])
    if a[i]==b:
        count+=1   
    i+=1
if count>=1:    
     print("YES")
else:
    print("NO")    
    