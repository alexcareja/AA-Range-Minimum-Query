from rmq_banal import RMQ_banal
from rmq_sparse import RMQSparse
from farach_colton_benders import RMQFCB
from Input_Class import Input

inp = Input()
for t in range(5,7):
	inp.readData(f"test{t}.in")
	#algo = RMQSparse(inp.getVector())
	algo = RMQFCB(inp.getVector())
	algo.preprocess()
	passed = True
	for (x, y) in inp.getIndexes():
		try:
			#assert RMQ_banal(inp.getVector(), x, y) == algo.RMQ(x, y)
			print(str(RMQ_banal(inp.getVector(), x, y)) + " " 
			+ str((algo.RMQ(x, y))))
		except AssertionError:
			passed = False
			print(f"test{t}.in" + "."*25 + "failed!\n")
			break
	if passed:
		print(f"test{t}.in" + "."*25 + "passed!")