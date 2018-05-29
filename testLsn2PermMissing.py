def solution(A):
    # write your code in Python 2.7
    A.sort()
    missing = False
    for i in range(1,len(A)+1):
    	if i != A[i-1]:
    		missing = True

    if missing:
    	return 0
    else:
    	return 1

print(solution([4,1,3]))