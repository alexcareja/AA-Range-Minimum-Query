from rmq_banal import RMQ_banal
from input_class import Input

#set number of tests
N_TESTS = 30

inp = Input()
for t in range(N_TESTS):
	inp.readData(f"in/test{t}.in")
	with open(f"out/test{t}.out", "w") as file:
		for (x, y) in inp.getIndexes():
			result = RMQ_banal(inp.getVector(), x, y)
			file.write(str(result))
			file.write("\n")
