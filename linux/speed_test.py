from functools import wraps
from time import time
from input_class import Input
from rmq_sparse import RMQSparse
from farach_colton_bender import RMQFCB
from segment_tree import RMQSegment
from rmq_banal import RMQ_banal
import sys

algo_name = sys.argv[1]

def speedTest(fn):
	@wraps(fn)
	def wrapper(*args):
		start_time = time()
		result = fn(*args)
		end_time = time()
		#print(f"Executing {fn.__name__}")
		print(f"Time elapsed: {end_time - start_time}\n")
		return result
	return wrapper

@speedTest
def preprocessAlgo(algo, *args):
	algo.printAlgo()
	print("Preprocessing")
	algo.preprocess()

@speedTest
def answerQueries(algo, indexes, *args):
	print("Answering queries")
	for (x, y) in indexes:
		algo.RMQ(x, y)

@speedTest
def testBasic(vector, indexes):
	print("Speed testing basic solution")
	for (x, y) in indexes:
		RMQ_banal(vector, x, y)
		

inp = Input()
inp.readData("in/big_test.in")
algo = None
if algo_name == "sparse":
	algo = RMQSparse(inp.getVector())
if algo_name == "cartesian":
	algo = RMQFCB(inp.getVector())
if algo_name == "segment":
	algo = RMQSegment(inp.getVector())
if algo_name == "basic":
	testBasic(inp.getVector(), inp.getIndexes())
	sys.exit()
if algo is None:
	raise Exception("Invalid argument")
	sys.exit()
preprocessAlgo(algo)
answerQueries(algo, inp.getIndexes())
