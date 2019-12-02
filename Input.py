
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

	def clean(self):
		self.vector = []
		self.indexes = []
		self.N = 0
		self.M = 0

	def readData(self, in_file):
		self.clean()
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
			