def solution(A):
    # write your code in Python 2.7
    countPairs = 0
    zeroCountBeforeOneIndex = 0
    prevZeroCountBeforeOneOndex = 0
    oneIndex = -1
    for i in range(len(A)):

    	if A[i] == 0:
    		if oneIndex == -1:
    			zeroCountBeforeOneIndex+=1
    		else:
    			prevZeroCountBeforeOneOndex = prevZeroCountBeforeOneOndex+zeroCountBeforeOneIndex
    			zeroCountBeforeOneIndex = 0
    			#oneIndex = -1
    			zeroCountBeforeOneIndex += 1 
    	elif A[i] == 1:
    		if oneIndex < i:
    			countPairs = countPairs + prevZeroCountBeforeOneOndex
    		
    		oneIndex = i
    		countPairs = countPairs + zeroCountBeforeOneIndex

    if countPairs > 1000000000:
    	return -1
    else:
    	return countPairs

# https://codility.com/demo/results/demoUCKPKF-QBH/
print(solution([0,0,1,1,1]))
print(solution([0,0,0,1,1]))
print(solution([0,0,1,0,1,0]))
print(solution([0,0,1,0,1,1]))
print(solution([1,0,1,1,0,1]))
print(solution([1,1,1,1,0,1]))
print(solution([0, 1, 0, 1, 0, 1]))