# a=["anuj", "bala", "chhaya", "deepu"]
b=["archana", "pooja", "rani", "aasma", "shivani", "shanti"]
# i=0
# z=0
# while i<len(b)-1:
#     j=i+1
#     while j<len(b):
#         print(b[i], "hand shake with",b[j])
#         z+=1
#         j+=1
#     i+=1
# print(z)    


# i=0
# count=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         print(a[i],"shook hand sake", b[j])
#         count+=1
#         j+=1
#     i+=1 
# print(count)



i = 0
count = 0
while i < len(b):
    j = 0
    while j < len(b):
        if b[i] != b[j]:
            print(b[i], "slap", b[j])
            count += 1
        j += 1
    i += 1
print(count)    

# i = 0
# count = 0
# while i < len(b):
#     j = 0
#     while j < len(b):
#         print(b[i], "choclate", b[j])
#         count += 1
#         j += 1
#     i += 1
# print(count)    

