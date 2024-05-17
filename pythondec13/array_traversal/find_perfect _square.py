a=[10,8,14,11,6,15]
i=0
count=0
while i<len(a):
    z=a[i]**0.5
    if z%1==0:
        count+=1
        break
    i+=1
    # break
if count==1:
    print(a[i])
else:
    print("No")        


# x=int(input())
# sqrt=x**0.5
# result=(sqrt)
# if result%1==0:
#     print(int(result),"Yes")
# else:
#     print("No")    