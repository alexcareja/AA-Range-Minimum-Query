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


class LCA():

	def __init__(self, n):
		self.n = n
		#self.adj = [[]]
		self.block_size = 0
		self.block_cnt = 0
		self.first_visit = []
		self.euler_tour = []
		self.height = []
		self.log_2 = []
		self.st = [[]]
		self.blocks = [[[]]]
		self.block_mask = []

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

	def min_by_h(self, i, j):
		if(i >= len(self.euler_tour)):
			i = len(self.euler_tour) - 1
		if(j >= len(self.euler_tour)):
			j = len(self.euler_tour) - 1
		a = self.euler_tour[i]
		b = self.euler_tour[j]
		if self.height[a] < self.height[b]:
			return i
		return j

	def precompute_lca(self, root):
		# get euler tour & indices of first occurences
		self.first_visit = [-1 for i in range(self.n)]
		self.height = [0 for i in range(self.n)]
		self.dfs(root, 0)

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
			if j == 0 or self.min_by_h(i, self.st[b][0]) == i:
				self.st[b][0] = i
			j += 1
		for l in range(1, self.log_2[self.block_cnt]):
			for i in range(self.block_cnt):
				ni = i + (1 << (l - 1))
				if ni >= self.block_cnt:
					self.st[i][l] = self.st[i][l-1]
				else:
					self.st[i][l] = self.min_by_h(self.st[i][l-1], self.st[ni][l-1])

		# precompute mask for each block
		self.block_mask = [0 for i in range(self.block_cnt)]
		j = 0
		b = 0
		for i in range(m):
			if j == self.block_size:
				j = 0
				b += 1
			if j > 0 and (i >= m or self.min_by_h(i - 1, i) == i - 1):
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
					print(self.blocks)
					self.blocks[mask][l][r] = self.blocks[mask][l][r-1]
					if b * self.block_size + r < m:
						print("self " + str(self.min_by_h(
							b * self.block_size + self.blocks[mask][l][r], 
							b * self.block_size + r) ))
						self.blocks[mask][l][r] = self.min_by_h(
							b * self.block_size + self.blocks[mask][l][r], 
							b * self.block_size + r) 
						- b * self.block_size
						#if self.blocks[mask][l][r] > 20:
						print(f"mask = {mask}, l = {l}, r = {r}")

	def lca_in_block(self, b, l, r):
		print("aici")
		print(self.blocks[self.block_mask[b]][l][r])
		return self.blocks[self.block_mask[b]][l][r] + b * self.block_size

	def lca(self, vector, v, u):
		print(self.first_visit)
		l = self.first_visit[v]
		r = self.first_visit[u]
		if l > r:
			l, r = r, l
		bl = l // self.block_size
		print(f"r = {r}")
		br = r // self.block_size
		print(f"br = {br}")
		print(f"block_size = {self.block_size}")
		if bl == br:
			return vector[self.euler_tour[
			self.lca_in_block(bl, 1 % self.block_size, r % self.block_size)]]
		ans1 = self.lca_in_block(bl, l % self.block_size, self.block_size - 1);
		ans2 = self.lca_in_block(br, 0, r % self.block_size);
		print(ans1)
		print(ans2)
		ans = self.min_by_h(ans1, ans2);
		if bl + 1 < br:
			l = self.log_2[br - bl - 1];
			ans3 = self.st[bl + 1][l];
			ans4 = self.st[br - (1 << l)][l];
			ans = self.min_by_h(ans, self.min_by_h(ans3, ans4));
		return vector[self.euler_tour[ans]]


vector = [83, 112, 163, 121, 85, 66, 120, 70, 195, 156, 20, 176, 156, 61, 4, 23, 141, 168, 82, 156, 106, 56, 21, 17, 176, 130, 164,
 56, 14, 132, 56, 116, 87, 167, 122, 103, 4, 119, 166, 11 ]
#vector = [6, 9, 2, 4, 7, 8, 5, 8, 3, 7]
N = len(vector)
parent = [-1 for i in range(N)]
stack = []
for i in range(N):
	last = -1
	while len(stack) != 0:
		if vector[stack[len(stack) - 1]] >= vector[i]:
			last = stack.pop()
		else:
			break
	if len(stack) != 0:
		parent[i] = stack[len(stack) - 1]
	if last >= 0:
		parent[last] = i
	stack.append(i)
#print(parent)
nodes = []
# crearea legaturilor din tree
i = 0
for num in vector:
	new_node = Node(num, i)
	nodes.append(new_node)
	if parent[i] == -1:
		root = new_node
	i += 1
for i in range(N):
	current_node = nodes[i]
	if parent[i] != -1:
		current_node.setParent(nodes[parent[i]])
		if parent[i] < i:
			nodes[parent[i]].setRight(current_node)
		else:
			nodes[parent[i]].setLeft(current_node)

rmq = LCA(N)
rmq.precompute_lca(root)
a = rmq.lca(vector, 0, 31)
print(a)