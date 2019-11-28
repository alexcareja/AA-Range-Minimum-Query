
class RMQSparse():
	PRINT = False

	def __init__(self, vector):
		self.vector = vector
		self. N = len(vector)
		# precompute log
		self.log = [-1, 0]
		for i in range(2, self.N + 1):
			self.log.append(self.log[i // 2] + 1)
		self.k = self.log[self.N] + 1
		self.st = [[0 for i in range(self.k)] for i in range(self.N)]

	def preprocess(self):
		# precompute table
		for i in range(self.N):
			self.st[i][0] = self.vector[i]
		for j in range(1, self.k + 1):
			i = 0
			while(i + (1 << j) <= self.N):
				self.st[i][j] = min(self.st[i][j-1], self.st[i + (1 << (j - 1))][j-1])
				i += 1
		

	def RMQ(self, x, y):
		z = self.log[y - x + 1]
		return min(self.st[x][z], self.st[y - (1 << z) + 1][z])

	def printAlgo(self):
		if RMQSparse.PRINT == False:
			print("Testing Sparse Table...")
			RMQSparse.PRINT = True

