# You are given an array of integers. Print an array where each index has the sum of all numbers in the original array except the number at that index.

# Avoid using subtraction, and handle this with nested loops.

# Sample Input
# 7 3 6 7 5

# Sample Output
# 21 25 22 21 23

# Explanation: The first element of the array is 7, so we print sum of all the elements except the number itself. 21 = 3 + 6 + 7 + 5.
# The second element of the array is 3. 25 = 7 + 6 + 7 + 5.
# The third element of the array is 6. 22 = 7 + 3 + 7 + 5.
# The fourth element of the array is 7. 21 = 7 + 3 + 6 + 5.
# The fifth element of the array is 5. 23 = 7 + 3 + 6 + 7.



a=[7, 3, 6, 7, 5]
# i=0
# sum=0
# while i<len(a):
#     sum+=a[i]
#     i+=1
# i=0
# while i<len(a):   
#     print(sum-a[i],end=" ")
#     i+=1




i=0
sum=0
while i <len(a):
    if i!=i:
        j=0
        while j<len(a):
            sum+=a[j]
            j+=1
        # sum+=a[i]
        # print(sum,end="")    
    i+=1       
print(sum)