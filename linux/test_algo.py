from rmq_banal import RMQ_banal
from rmq_sparse import RMQSparse
from farach_colton_bender import RMQFCB
from segment_tree import RMQSegment
from input_class import Input
import filecmp
import sys

N_TESTS = 30
DOTS = 31

algo_name = sys.argv[1]
inp = Input()
for t in range(N_TESTS):
	inp.readData(f"in/test{t}.in")
	algo = None
	if algo_name == "sparse":
		algo = RMQSparse(inp.getVector())
	if algo_name == "cartesian":
		algo = RMQFCB(inp.getVector())
	if algo_name == "segment":
		algo = RMQSegment(inp.getVector())
	if algo is None:
		raise Exception("Invalid argument")
		sys.exit()
	algo.preprocess()
	algo.printAlgo()
	passed = True
	with open(f"test{t}.out", "w") as file:
		for (x, y) in inp.getIndexes():
			result = algo.RMQ(x, y)
			file.write(str(result))
			file.write("\n")

for t in range(N_TESTS):
	refFile = f"out/test{t}.out"
	outFile = f"test{t}.out"
	if filecmp.cmp(	refFile, outFile):
		print(f"test{t}.in" + "."*(DOTS-len(str(t))) + "passed!")
	else:
		print(f"test{t}.in" + "."*(DOTS-len(str(t))) + "failed!\n")

