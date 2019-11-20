
vector = [22, 123, 2, 10, 25, 6, 90, 95, 92, 1, 5, 7]
N = len(vector)
parent = [-1 for i in range(N)]
stack = []
for i in range(12):
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
print(stack)
print(parent)