a=[3,6, 22, 11, 8, 2, 5, 7, 1]
i=0
b=[]
while i<len(a)-1:
    # print(a[i]+a[i+1])
    b=b+[a[i]+a[i+1]]   
    i+=1 
print(b)
max=b[0]
j=1
while j<len(b):
    if b[j] > max:
        max = b[j]
    j+=1
print(max)      
