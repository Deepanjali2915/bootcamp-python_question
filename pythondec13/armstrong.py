a=int(input())
b=len(str(a))
sum=0
m=a 
while m>0:
    z=m%10
    x=z**b
    sum+=x
    m//=10
print(sum)    
if (a)==sum:
    print("Yes")
else:
    print("NO")    