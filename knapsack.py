# Dynamic Programming
def knapsack(W, V, M):
	wLen = len(W)
	K = [0] * (M + 1)
	best = 0
	for w in range(1, M + 1):
		for i in range(wLen):
			if w >= W[i]:
				best = max((K[w - W[i]]) + V[i], best)
				#print(best)

		K[w] = best
		#print(K)

	return K[M]

print(knapsack([6,3,4,2], [30, 14, 16, 9], 10))
