# You are given an array of integers. Find the minimum and maximum difference between any two elements in an array.

# Sample Input
# 5 4 7 8 4 6 11 9

# Sample Output
# 0 7

# Explanation: Minimum Difference: 4 - 4 = 0. Maximum Difference: 11 - 4 = 7



# a=[5, 3, 7, 8, 4, 6, 11, 9]
a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# a=[6, 8, 10, 12, 16, 21, 25]
# a = [2,4,6,8,9,7,10,14,1,4,12]
# a=[6, 8, 10, 12, 16, 21, 25]
min = a[0]
max = 0
i = 0
while i < len(a)-1:
    j=i+1
    while j < len(a):
        diff = abs(a[j]-a[i])
        if diff < min:
            min = diff  
        elif diff > max:
            max = diff    
        j+=1    
    i+=1 
print(min, max)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# a=[6, 8, 10, 12, 16, 21, 25]
# i=0
# min=0
# while i<len(a)-1:
#     j=i+1 
#     while j<len(a):
#         deff=abs(a[i]-a[j])
#         if deff<min:
            


