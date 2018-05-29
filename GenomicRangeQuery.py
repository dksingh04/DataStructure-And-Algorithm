def solution(S, P, Q):
    # write your code in Python 2.7
   
    result = []
  
    for index in range(len(P)):
    	
    	if (S[P[index]:(Q[index]+1)]).find("A") >= 0:
    		result.append(1)
    	elif (S[P[index]:(Q[index]+1)]).find("C") >= 0:
    		result.append(2)
    	elif (S[P[index]:(Q[index]+1)]).find("G") >= 0:
    		result.append(3)
    	elif (S[P[index]:(Q[index]+1)]).find("T") >= 0:
    		result.append(4)

    return result
    
    
#https://codility.com/demo/results/demo57KMQ9-ESX/

print(solution("CAGCCTA", [2,5,0], [4,5,6]))