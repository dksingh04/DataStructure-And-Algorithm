def solution(X, A):
    # write your code in Python 2.7
    previousNums = set()
    second = -1
    found = False
    for i in range(len(A)):
       if A[i] == X:
           found = True
           if len(previousNums) == X - 1:
               prevSum = sum(previousNums)
               totalSum = prevSum + X
               if totalSum - prevSum == X:
                   second = i
                   break
                
       else:
           previousNums.add(A[i])
           if found and len(previousNums) == X - 1:
               prevSum = sum(previousNums)
               totalSum = prevSum + X
               if totalSum - prevSum == X:
                   second = i
                   break
           
		   
    
    return second

#https://codility.com/demo/results/training9GSX4N-6UW/
print(solution(5, [1,3,1,4,2,3,5,4]))
print(solution(3, [1,3,3,3,2,3,5,4]))