
class Node():
	
	def __init__(self, num, index):
		self.num = num
		self.index = index
		self.parent = None
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.num)

	def getIndex(self):
		return self.index

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setParent(self, node):
		self.parent = node

	def setLeft(self, node):
		self.left = node

	def setRight(self, node):
		self.right = node
