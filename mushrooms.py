def prefix_sums(A):
	n = len(A)
	p = [0] * (n+1)

	for k in range(1,n+1):
		p[k] = p[k-1] + A[k-1]

	return p

def count_total(P, x, y):
	return P[y+1] - P[x]

#print(prefix_sums([2,3,7,5,1,3,9]))

#print(count_total(prefix_sums([2,3,7,5,1,3,9]), 4, 6))

def mushroom(A, k, m):
	n = len(A)
	result = 0
	prefSums = prefix_sums(A)

	print("prefSums: ", prefSums)

	for p in range(min(m, k)):
		left_pos = k - p
		right_pos = min(n-1, max(k, k + m - 2 * p))
		print("left_pos: "+str(left_pos)+" right_pos: "+str(right_pos))
		result = max(result, count_total(prefSums, left_pos, right_pos))
		print("result: ", result)

	for p in range(min(m + 1, n - k)):
		right_pos = k + p
		left_pos = max(0, min(k, k - (m - 2 * p)))
		print("right_pos: "+str(right_pos)+" left_pos: "+str(left_pos))
		result = max(result, count_total(prefSums, left_pos, right_pos))
		print("result: ", result)

	return result

print(mushroom([2,3,7,5,1,3,9], 4, 3))

