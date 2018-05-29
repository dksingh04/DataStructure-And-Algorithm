def solution(A, B, K):
    # write your code in Python 2.7
    counter = 0
    
    if A%K == 0:
    	counter = 1
    
    counter = B//K - A//K + counter

    
    return counter

#https://codility.com/demo/results/demoT4ECUZ-F48/
#print(solution(6, 11, 9))