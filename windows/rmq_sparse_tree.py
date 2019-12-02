
class RMQSparse():

	def __init__(self, vect):
		self.vect = vect
		self. N = vect.size()
		self.lookup = [[0 for i in range(N)] for i in range(N)]

	def preprocess(self, vect, N):
		print(self.lookup)
		pass

	def RMQ_Sparse_Table(self):
		pass