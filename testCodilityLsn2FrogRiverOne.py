def solution(X, A):
    # write your code in Python 2.7
    posHaveSeconds = [-1] * (X+1)
    posHaveSeconds[0] = -2
    for k in range(len(A)):
    	if posHaveSeconds[A[k]] == -1:
    		posHaveSeconds[A[k]] = k

    if posHaveSeconds.count(-1) > 0:
    	return -1
    else:
    	return max(posHaveSeconds)

print(solution(5, [1,3,1,1,2,3,5,4]))