from node import Node

class RMQFCB():

	def __init__(self, vector):
		self.vector = vector
		self.n = len(vector)
		self.root = None
		self.block_size = 0
		self.block_cnt = 0
		self.fist_visit = []
		self.euler_tour = []
		self.height = []
		self.log_2 = []
		self.st = [[]]
		self.blocks = [[[]]]
		self.block_mask = []

	def buildCartesianTree(self):
		parent = [-1 for i in range(self.n)]
		stack = []
		for i in range(self.n):
			last = -1
			while len(stack) != 0:
				if self.vector[stack[len(stack) - 1]] >= self.vector[i]:
					last = stack.pop()
				else:
					break
			if len(stack) != 0:
				parent[i] = stack[len(stack) - 1]
			if last >= 0:
				parent[last] = i
			stack.append(i)
		nodes = []
		# crearea legaturilor din tree
		i = 0
		for num in self.vector:
			new_node = Node(num, i)
			nodes.append(new_node)
			if parent[i] == -1:
				self.root = new_node
			i += 1
		for i in range(self.n):
			current_node = nodes[i]
			if parent[i] != -1:
				current_node.setParent(nodes[parent[i]])
				if parent[i] < i:
					nodes[parent[i]].setRight(current_node)
				else:
					nodes[parent[i]].setLeft(current_node)

	def dfs(self, node, h):
		if(node == None):
			return
		v = node.getIndex()
		self.first_visit[v] = len(self.euler_tour)
		self.euler_tour.append(v)
		self.height[v] = h
		next_node = node.getLeft()
		if(next_node != None):
			self.dfs(next_node, h + 1)
			self.euler_tour.append(v)
		next_node = node.getRight()
		if(next_node != None):
			self.dfs(next_node, h + 1)
			self.euler_tour.append(v)

	def minByH(self, i, j):
		a = self.euler_tour[i]
		b = self.euler_tour[j]
		if self.height[a] < self.height[b]:
			return i
		return j


	def lcaPrecompute(self):
		# get euler tour & indices of first occurences
		self.first_visit = [-1 for i in range(self.n)]
		self.height = [0 for i in range(self.n)]
		self.dfs(self.root, 0)

		# precompute all log values
		m = len(self.euler_tour)
		self.log_2.append(-1)
		for i in range(1, m + 1):
			self.log_2.append(self.log_2[i // 2] + 1)

		self.block_size = max(1, self.log_2[m] // 2)
		self.block_cnt = (m + self.block_size -1) // self.block_size

		# precompute minimum of each block and build sparse table
		self.st = [ [0 for j in range(self.log_2[self.block_cnt] + 1)] 
					for i in range(self.block_cnt) ]
		j = 0
		b = 0
		for i in range(m):
			if j == self.block_size:
				j = 0
				b += 1
			if j == 0 or self.minByH(i, self.st[b][0]) == i:
				self.st[b][0] = i
			j += 1
		for l in range(1, self.log_2[self.block_cnt]):
			for i in range(self.block_cnt):
				ni = i + (1 << (l - 1))
				if ni >= self.block_cnt:
					self.st[i][l] = self.st[i][l-1]
				else:
					self.st[i][l] = self.minByH(self.st[i][l-1], self.st[ni][l-1])

		# precompute mask for each block
		self.block_mask = [0 for i in range(self.block_cnt)]
		j = 0
		b = 0
		for i in range(m):
			if j == self.block_size:
				j = 0
				b += 1
			if j > 0 and (i >= m or self.minByH(i - 1, i) == i - 1):
				self.block_mask[b] += 1 << (j - 1) 
			j += 1

		# precompute RMQ for each block
		possibilities = 1 << (self.block_size - 1)
		self.blocks = [[] for i in range(possibilities)]
		for b in range(self.block_cnt):
			mask = self.block_mask[b]
			if len(self.blocks[mask]) != 0:
				continue
			self.blocks[mask] = [ [0 for i in range(self.block_size)] 
								for j in range(self.block_size) ]
			for l in range(self.block_size):
				self.blocks[mask][l][l] = l
				for r in range(l+1, self.block_size):
					self.blocks[mask][l][r] = self.blocks[mask][l][r-1]
					if b * self.block_size + r < m:
						self.blocks[mask][l][r] = self.minByH(
							b * self.block_size + self.blocks[mask][l][r], 
							b * self.block_size + r) 
						- b * self.block_size

	def lcaInBlock(self, b, l, r):
		return self.blocks[self.block_mask[b]][l][r] + b * self.block_size

	def lca(self, v, u):
		l = self.first_visit[v]
		r = self.first_visit[u]
		if l > r:
			l, r = r, l
		bl = l // self.block_size
		br = r // self.block_size
		if bl == br:
			return self.vector[self.euler_tour[
			self.lcaInBlock(bl, 1 % self.block_size, r % self.block_size)]]
		ans1 = self.lcaInBlock(bl, l % self.block_size, self.block_size - 1);
		ans2 = self.lcaInBlock(br, 0, r % self.block_size);
		ans = self.minByH(ans1, ans2);
		if bl + 1 < br:
			l = self.log_2[br - bl - 1];
			ans3 = self.st[bl + 1][l];
			ans4 = self.st[br - (1 << l)][l];
			ans = self.minByH(ans, self.minByH(ans3, ans4));
		return self.vector[self.euler_tour[ans]]

	def preprocess(self):
		self.buildCartesianTree()
		self.lcaPrecompute()

	def RMQ(self, x, y):
		return self.lca(x, y)

#vector = [5, 123, 24, 120, 25, 6, 90, 95, 92, 1, 5, 7, 21, 42, 2, 1, 4, 5, 22, 10, 3, 99, 1, 4]
#farach = RMQFCB(vector)
#farach.preprocess()
#print(farach.RMQ(0, 1))