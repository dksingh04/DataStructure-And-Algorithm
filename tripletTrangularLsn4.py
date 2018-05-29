def solution(A):
    # write your code in Python 2.7
    A.sort()
    lenA = len(A)
    if lenA < 3:
    	return 0
    # sort the array and now A[index] < A[index+1] and A[index+2], similarliy A[index+1] < A[index+2]
    # and A[index+1] + A[index+2] > A[index] and A[index] + A[index+2] > A[index+1] so we have to onely check
    # A[index] + A[index+1] > A[index + 2]

    for index in xrange(lenA - 2):
    	if A[index] + A[index+1] > A[index+2]:
    		return 1

    return 0
    
    #https://codility.com/demo/results/demoNY86Y4-92F/