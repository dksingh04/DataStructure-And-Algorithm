def solution(A):
    # write your code in Python 2.7
    s = set([])
    for i in range(len(A)):
    	s.add(A[i])

    return len(s)

print(solution([2,1,1,2,3,1]))
#https://codility.com/demo/results/demoJYU6U9-GTC/