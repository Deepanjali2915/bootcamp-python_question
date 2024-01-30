A = [64, 5, 1, 22, 101]

## Traverse through all array elements
#for i in range(len(A)):
    ## Find the minimum element in remaining unsorted array
    #min_idx = i
    #for j in range(i + 1, len(A)):
       # if A[min_idx] > A[j]:
      #      min_idx = j

    ### Swap the found minimum element with the first element
   # A[i], A[min_idx] = A[min_idx], A[i]

### Driver code to test above
#print("Sorted array")
#for i in range(len(A)):
 #   if i == len(A) - 1:
  #      print(A[i], end=" ")
   # else:
    #    print( A[i], end=" ")





print("unsorted list",A)

for i in range(len(A)-1):
    m_ind=i
    for j in range(i+1,len(A)):
        if A[j]>A[m_ind]:
            m_ind=j
    if A[i]!=A[m_ind]:
        A[i],A[m_ind]=A[m_ind],A[i]
print(A)        
    
