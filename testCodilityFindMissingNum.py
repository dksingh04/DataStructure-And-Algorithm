def solution(A):
    # write your code in Python 2.7
    n = len(A)
    if n >= 1:
        sumationOfSeries = (n*(n+1))/2
        sumOfArray = sum(A)
        diff = abs(sumOfArray-sumationOfSeries)
        maximumVal = max(A)
        if diff == 0:
            return maximumVal+1
        else:
            return maximumVal-diff
    
    else:
        return 1

print(solution([2,3,1,4]))
print(solution([]))
print(solution([2]))
print(solution([1]))
print(solution([1,2,3,4,6]))