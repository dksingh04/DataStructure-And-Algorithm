import math
def solution(X, Y, D):
    # write your code in Python 2.7
    diff = Y - X
    steps = math.ceil(diff/D)
    coveredDistance = X + (D*steps)
    if coveredDistance == Y:
        return steps
    else:
        return steps+1

print(solution(5, 100, 25))