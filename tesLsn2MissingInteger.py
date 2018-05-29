def solution(A):
    # write your code in Python 2.7
    
    numCount = [0] * (len(A)+1)
   
    for x in range(1,len(A)+1):
    	if A[x-1]>0:
    		numCount[A[x-1]-1] = A[x-1]
    
    
    index = numCount.index(0)
   
    return index+1

print(solution([1,3,3,3,1,2]))

#https://codility.com/demo/results/demo7663YN-N7R/