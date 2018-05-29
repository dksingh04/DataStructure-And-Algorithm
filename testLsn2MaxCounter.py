def solution(N, A):
    # write your code in Python 2.7
    maxcounters = [0]*N
    maxVal = 0
    for k in range(len(A)):
    		if A[k] <= N:
    			maxcounters[A[k]-1] += 1
    			if maxVal == 0 or maxVal < maxcounters[A[k]-1]:
    				maxVal = maxcounters[A[k]-1]
    				#print(maxVal)
    		if A[k] == N+1:
    			maxcounters = [maxVal] * N
    		
    		#print(maxcounters)

   # print(maxcounters)

    return maxcounters

print(solution(5,[3,4,4,6,4,6,4]))
print(solution(1, [2, 1, 1, 2, 1]))

# Check result from here
#https://codility.com/demo/results/demo3REW7X-FGM/
#print(solution(5,[3,4]))
#print(solution(5,[3,4]))