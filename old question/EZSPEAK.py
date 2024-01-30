t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    ccount=0
    for i in range(0,len(s)):   
        if s[i] not in ("a","e","i","o","u","A","E","I","O","U"):  
            ccount+=1
            if ccount==4:
                break
         else:
            ccount=0       
    if ccount<4:
        print("YES")
    else:
        print("NO")    


