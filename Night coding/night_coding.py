a=input()
i=len(a)
c=0
while i>0:
	if a[i]==1:
		b=2**i
		c+=b
	i-=1
print(c)	
