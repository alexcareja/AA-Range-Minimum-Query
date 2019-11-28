from random import randint

#change to diversify tests
NO_TESTS = 30
MAX_INT = 500000
MIN_QUERIES = 10
N = 500
#b = randint(0, 4000)
#M = max(MIN_QUERIES , b)
M = 100000

def genIndexTuple(N):
	(x, y) = (randint(0, N - 1), randint(0,N - 1))
	if x > y:
		(x, y) = (y, x)
	return (x, y)

def genInFile(index):
	"""
	Output files format:
		First line: N
		Second line: M
		Third line: N integers (elements of the array)
		Next M lines: Pairs of indexes for RMQ queries
	"""
	vector = []
	for i in range(0,N):
		vector.append(randint(0, MAX_INT))
	indexes = []
	for i in range(0, M):
		while True:
			(x, y) = genIndexTuple(N)
			if (x, y) not in indexes and x != y:
				indexes.append((x, y))
				break
	with open(f"test{index}.in", "w") as file:
		file.write(str(N) + '\n')
		file.write(str(M) + '\n')
		for num in vector:
			file.write(str(num) + " ")
		for (x, y) in indexes:
			file.write("\n" + str(x) + " " + str(y))
	return

for i in range(1):
	genInFile(i)
