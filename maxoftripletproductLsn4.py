def solution(A):
    # write your code in Python 2.7
    A.sort()
    result = 0

    if A[0] < 0 and A[1] < 0:
    	result = (A[0] * A[1] * A[len(A) - 1])
    
    if result < (A[len(A)-1] * A[len(A)-2] * A[len(A)-3]):
    	result = (A[len(A)-1] * A[len(A)-2] * A[len(A)-3])

    return result


#https://codility.com/demo/results/demoV7ZENP-QR8/