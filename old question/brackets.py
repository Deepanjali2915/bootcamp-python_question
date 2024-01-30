a=input()
count=0
i=0
while i<len(a):
    if a[i]=="(":
        count+=1
    elif a[i]==")":
        count-=1
    if count<0:
        break
    i+=1
if count!=0:
    print("N")
else:
    print("Y")
