t=int(input())
for i in range(t):
    a,b,c,m=map(int,input().split())
    if ((a+m)==b and b!=c and c!=(a+m)) or ((b+m)==c and c!=a and a!=(b+m)) or ((c+m)==a and a!=b and b!=(c+m)) or (a==b and b!=c and c!=a) or (a==c and a!=b and b!=c) or (b==c and c!=a and a!=b)or ((a+m)==c and c!=b and b!=(a+m)) or ((b+m)==a and a!=c and c!=(b+m)) or ((c+m)==b and b!=a and a!=(c+m)):
        print("YES")
    else:
        print("NO")
        