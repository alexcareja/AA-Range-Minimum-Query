from rmq_banal import RMQ_banal
from rmq_sparse import RMQSparse
from farach_colton_benders import RMQFCB
from segment_tree import RMQSegment
from Input_Class import Input
import filecmp

N_TESTS = 11
DOTS = 31

inp = Input()
for t in range(0,N_TESTS):
	inp.readData(f"in/test{t}.in")
	#algo = RMQSparse(inp.getVector())
	algo = RMQFCB(inp.getVector())
	#algo = RMQSegment(inp.getVector())
	algo.preprocess()
	passed = True
	with open(f"out/test{t}.out", "w") as file:
		for (x, y) in inp.getIndexes():
			result = algo.RMQ(x, y)
			file.write(str(result))
			file.write("\n")

for t in range(0,N_TESTS):
	refFile = f"ref/test{t}.ref"
	outFile = f"out/test{t}.out"
	if filecmp.cmp(refFile, outFile):
		print(f"test{t}.in" + "."*(DOTS-len(str(t))) + "passed!")
	else:
		print(f"test{t}.in" + "."*(DOTS-len(str(t))) + "failed!\n")

