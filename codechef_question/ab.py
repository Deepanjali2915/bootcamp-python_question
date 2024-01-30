N=int(input())
S=str(input())
i=0
y=" "
while i<N:
    if S[i]=="a" and S[i+1]=="b":
        y=y+"YES"
    elif S[i]=="b" and S[i+1]=="a":  
        y=y+"YES"  
    else:
        y=y+"NO"
    i+=1          
print(y)    
