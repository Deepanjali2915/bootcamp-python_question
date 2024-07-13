a=[1,2,3,4,6,1] 
sum=17
sum-a[0] or sum-a[n-1]
sum%2
	print(n-1  ) 
sum-(a[0]+a[1]) or sum-(a[n-1]+a[n-2]) 
sum%2
	print(n-2)
sum-(a[0]+a[1]+a[2]) or sum-(a[n-1]+a[n-2]+a[n-3]) 
sum%2
	print(n-3)
		
	    	
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    sum=0
    while i<len(a):
        sum+=a[i]
        i+=1 
    j=0
    suma=0
    sumb=0
    while j<len(a):
        suma+=a[j]
        sumb=sumb+a[n-1-j]
        j+=1
   #print(suma,sumb)
    k=0
    while k<len(x):
        if suma%2==0 and sumb%2==0:
            print(n)
        elif (sum-suma)%2==0 or (sum-sumb)%2==0:
            print(n-k)
        k+=1    
    
















	    	
	
