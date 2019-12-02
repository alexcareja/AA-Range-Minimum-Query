from random import randint

MAX_INT = 10000
def genIndexTuple(N):
	(x, y) = (randint(0, N - 1), randint(0,N - 1))
	if x > y:
		(x, y) = (y, x)
	return (x, y)

def genInFile(index):
	"""
	Formatul fisierelor de iesire va fi: 
		Pe prima linie N
		Pe a doua linie M
		Pe urmatoarea linie N intregi, reprezentand elementele vectorului
		Pe urmatoarele M linii, perechile de indecsi pentru RMQ
	"""
	N = 15000
	M = 15000
	vector = []
	for i in range(0,N):
		vector.append(randint(0, MAX_INT))
	indexes = []
	for i in range(0, M):
		while True:
			(x, y) = genIndexTuple(N)
			if (x, y) not in indexes and x != y:
				indexes.append((x, y))
				break;
	with open(f"test{index}.in", "w") as file:
		file.write(str(N) + '\n')
		file.write(str(M) + '\n')
		for num in vector:
			file.write(str(num) + " ")
		for (x, y) in indexes:
			file.write("\n" + str(x) + " " + str(y))
	return

for i in range(10,11):
	genInFile(i)