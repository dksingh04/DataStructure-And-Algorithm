def solution(A):
    # write your code in Python 2.7
    minAvgValue = (A[0] + A[1])/2
    minAvgPos = 0

    for index in range(len(A) - 2):
    	minAvegValue2 = (A[index] + A[index + 1]) / 2.0
    	if minAvegValue2 < minAvgValue:
    		minAvgValue = minAvegValue2
    		minAvgPos = index

    	minAvegValue3 = (A[index] + A[index+1] + A[index+2])/3.0

    	if minAvegValue3 < minAvgValue:
    		minAvgValue = minAvegValue3
    		minAvgPos = index

    minAvegValue2 = (A[len(A) - 1] + A[len(A) - 2])/2.0
    if minAvegValue2 < minAvgValue:
    	minAvgValue = minAvegValue2
    	minAvgPos = len(A) - 2

    return minAvgPos

print(solution([4,2,2,5,1,5,8]))

#https://codility.com/demo/results/demoSAF9Y8-GQS/
