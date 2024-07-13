# You are given an array of integers. Find the element that appears the maximum number of times in an array. 
# If multiple elements appear maximum number of times, you have to print the element which occurs first.

# Sample Input
# 5 4 7 11 8 4 6 11 9
# Sample Output
# 4
# Explanation: Both 4 and 11 appear 2 times. We can print any of 4 and 11, so we print 4.




# a=[3,6, 2, 1, 7, 3, 7, 4, 1, 7, 4]
a=[1, 1, 1, 1, 5,5,5,5, 4, 9]
i=0
count=0
while i<len(a)-1:
    if a[i]==a[i+1]:
        count+=1
    i+=1    
print(count)    


# i=0
# b=[]
# while i<len(a)-1:
#     # print(a[i]+a[i+1])
#     b=b+[a[i]+a[i+1]]   
#     i+=1 
# print(b)
# max=b[0]
# j=1
# while j<len(b):
#     if b[j] > max:
#         max = b[j]
#     j+=1
# print(max)      
  