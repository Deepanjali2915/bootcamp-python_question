t=int(input())
for _ in range(t):
    n=input()
    for i in range(len(n)):
        for j in range(i+1,(len(n))):
            print(n[i:j],end="*") 
        print()                                                                            
