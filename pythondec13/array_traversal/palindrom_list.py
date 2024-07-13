a=[11,1,13,21,3,7]
i=len(a)
b=[]
while i>0:  
    i-=1
    b.append(a[i]) 
#print(a)
#print(b)    
j=0
sum=0
while j <len(a):
    if  a[j]==b[j]:
        print(a[j],b[j])
        sum+=1
    j+=1
print(sum)
