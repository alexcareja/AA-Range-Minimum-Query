def RMQ_banal(vector, x, y):
	min = vector[x]
	for i in range(x + 1, y + 1):
		if vector[i] < min:
			min = vector[i]
	return min