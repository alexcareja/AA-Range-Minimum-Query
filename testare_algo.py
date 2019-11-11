from rmq_banal import RMQ_banal
from rmq_sparse import RMQSparse

class Input():

	def __init__(self):
		self.vector = []
		self.indexes = []
		self.N = 0
		self.M = 0

	def getVector(self):
		return self.vector

	def getIndexes(self):
		return self.indexes

	def readData(self, in_file):
		data = []
		with open(in_file, "r") as file:
			for line in file:
				line_int = list(map(int, line.split()))
				for num in line_int:
					data.append(num)
		data.reverse()
		self.N = data.pop()
		self.M = data.pop()
		for i in range(self.N):
			self.vector.append(data.pop())
		for i in range(self.M):
			(x, y) = (data.pop(), data.pop())
			self.indexes.append((x, y))

inp = Input()
for i in range(10, 11):
	inp.readData(f"test{i}.in")
	sparse = RMQSparse(inp.getVector())
	sparse.preprocess()
	passed = True
	for (x, y) in inp.getIndexes():
		try:
			assert RMQ_banal(inp.getVector(), x, y) == sparse.RMQ(x, y)
		except AssertionError:
			passed = False
			print(f"Failed test{i}.in!\n")
			break
	if passed:
		print(f"test{i}.in passed")