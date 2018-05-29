import random
def solution(A):
    result = []
    p1 = 0
    p2 = sum(A)
    
    for i in range(len(A)-1):
        p1 = p1 + A[i]
        p2 = p2 - A[i]
        difference = abs(p1 - p2)
        result.append(difference)

    result.sort()
    return result[0]


