a=[4,9,2,5,7,4,4,4,3]
# b=[9,6,4,8,6,1,12]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]==b[j]:
#             c=c+[a[i]]
#         j+=1 
#     i+=1 
# print(c)           
i=0
count=0
while i<len(a):
    j=1
    while j<len(a):
        if a[i]==a[j]:
            # print(a[i])
            count+=1
            # break
        j+=1
    i+=1
    if count==1:
        print(a)
