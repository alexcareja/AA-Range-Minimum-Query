def RMQ_banal(vector, x, y):
	min_el = vector[x]
	for i in range(x + 1, y + 1):
		if vector[i] < min_el:
			min_el = vector[i]
	return min_el