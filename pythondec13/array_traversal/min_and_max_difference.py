# You are given an array of integers. Find the minimum and maximum difference between any two elements in an array.

# Sample Input
# 5 4 7 8 4 6 11 9

# Sample Output
# 0 7

# Explanation: Minimum Difference: 4 - 4 = 0. Maximum Difference: 11 - 4 = 7



# a=[5, 4, 7, 8, 4, 6, 11, 9]
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
a=[6, 8, 10, 12, 16, 21, 25]
min = 0
max = 0
b=[]
i = 0
while i < len(a):
    j=i+1
    while j < len(a):
        deff = abs(a[i]-a[j])
        if deff <= min:
            min = deff
        elif deff > max:
            max = deff    

        j+=1 
    i+=1            
print(min, max)


