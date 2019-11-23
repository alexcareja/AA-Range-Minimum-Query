
class RMQSparse():

	def __init__(self, vector):
		self.vector = vector
		self. N = len(vector)
		self.lookup = [[0 for i in range(self.N)] for i in range(self.N)]

	def preprocess(self):
		for i in range(self.N):
			self.lookup[i][i] = i
		for i in range(self.N):
			for j in range(i + 1, self.N):
				if(self.vector[self.lookup[i][j - 1]] < self.vector[j]):
					self.lookup[i][j] = self.lookup[i][j - 1]
				else:
					self.lookup[i][j] = j

	def RMQ(self, x, y):
		return self.vector[self.lookup[x][y]]